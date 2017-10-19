import numpy as np
import os
import sys
import getopt

import keras.layers as kl
import keras.models as km

# the number of events types, also the dimension of each single input and output
DIM = 20

# return a sorted list of all files name
def sort_file_list(path):
    flist = os.listdir(path)
    index = flist[0].find('.')
    postfix = flist[0][index:]
    prefix = []
    for f in flist:
        prefix.append(int(f.split('.')[0]))
    prefix.sort()
    flist = []
    for p in prefix:
        flist.append(os.path.join(path,str(p) + postfix))
    return flist

def gen_dataset(path):
    flist = sort_flie_list(path)
    dataset = np.zeros([len(flist), DIM])
    for i in range(len(flist)):
        dataset[i] = build_event_vec(flist[i])
    return dataset
        
# build a vector to represent the event type distibution
def build_event_vec(fileName):
    vec = np.zeros(DIM, dtype=np.int32)
    with open(fileName, 'r') as f:
        line = f.readline()
        line = f.readline().strip('\n')
        while line != '':
            temp = line.split(': ')
            try:
                vec[int(temp[0])-1] = int(temp[1])
            except Exception:
                pass
                #print(fileName, line)
            line = f.readline().strip('\n')
    return vec

# build a raw dataset containing a series of event type distribution
def build_event_dataset(flist, start=0, end=None):
    dataset = np.zeros((end-start, DIM), dtype=np.int32)
    if end == None:
        end = len(flist)
    for i in range(start, end):
        dataset[i-start,:] = build_event_vec(flist[i])
    return dataset

# build dataset used for rnn training
def build_train_data(flist, start, end, step):
    trainSet = np.zeros((end-start, step, DIM), dtype=np.int32)
    for i in range(start, end):
        trainSet[i-start,:,:] = build_event_dataset(flist, i, i+step)
    return trainSet

# build dataset used for rnn test
def build_train_result(flist, start, end, step, lookahead):
    trainResult = np.zeros((end-start, 1, DIM), dtype=np.int32)
    for i in range(start, end):
        trainResult[i-start,:,:] = build_event_dataset(flist, i+step+lookahead, i+step+lookahead+1)

    trainResult = np.reshape(trainResult, (end-start,DIM))    
    return trainResult

# write a two-dimension data into a file
def write_result(filename, data):
    with open(filename, 'w') as f:
        for line in data:
            for e in line:
                f.write(str(e) + ' ')
            f.write('\n')

# build datasets
def build_datasets(path, trainSize=1500, testSize=60, step=30, lookahead=1):
    print('build training data')
    flist = sort_file_list(path)# build training and test datasets
    trainData = build_train_data(flist, 0, trainSize, step)
    print('build training result')
    #result = build_train_result(flist, 0, trainSize, step, lookahead)
    trainResult = build_train_data(flist, lookahead, trainSize+lookahead, step)
    print('build test data')
    testData = build_train_data(flist, trainSize, trainSize+testSize, step)
    print('build test result')
    #testResult = build_train_result(flist, trainSize, trainSize+testSize, step, lookahead)
    testResult = build_train_data(flist, trainSize+lookahead, trainSize+testSize+lookahead, step)
    print('all datasets built')
    return trainData, trainResult, testData, testResult

# train model
def train_model(trainData, trainResult, step=30, epochs=3000):
    model = km.Sequential()
    model.add(kl.LSTM(DIM, input_shape=(step, DIM), return_sequences=True, activation='relu'))
    #model.add(kl.LSTM(DIM, input_dim = DIM, input_length = step, activation='sigmoid'))
    model.add(kl.TimeDistributed(kl.Dense(DIM)))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainData, trainResult, epochs=epochs, batch_size=32, verbose=2, validation_split = 0.05)
    return model

# predict and evaluate
def eval_model(predict, testResult):
    errorSum = 0
    for i in range(predict.shape[0]):
        for j in range(predict.shape[1]):
            diff = sum(abs(predict[i,j,:] - testResult[i,j,:])) / sum(testResult[i,j,:])
            errorSum += diff
    errorAve = errorSum / predict.shape[0] / predict.shape[1]
    return errorAve

def main():
    path, modelFile = 'attr-aus', None
    epochs = 3000
    lookahead = 1
    step = 30
    # parse arguments
    options,args = getopt.getopt(sys.argv[1:],"p:a:e:m:s:")
    for opt, para in options:
        if opt == '-p':
            path = para
        if opt == '-a':
            lookahead = int(para)
        if opt == '-e':
            epochs = int(para)
        if opt == '-m':
            model = para
        if opt == '-s':
            step = int(para)
    trainData, trainResult, testData, testResult = build_datasets(path, step=step, lookahead=lookahead)
    if modelFile == None:   # train a new model
        model = train_model(trainData, trainResult, step=step, epochs=epochs)
        # save model
        model.save('model_%s_%d_%d_%d.h5'%(path, epochs, step, lookahead))
        print('model saved as: currentDirectory/model.h5')
    else:   # load a model
        print('load model from: ' + modelFile)
        model = km.load_model(modelFile)
    # predict
    predictResult = model.predict(testData)
    x,y = np.zeros([predictResult.shape[0],min(lookahead,step),DIM]), np.zeros([predictResult.shape[0],min(lookahead,step),DIM])
    for i in range(predictResult.shape[0]):
        x[i] = predictResult[i,-lookahead:]
        y[i] = testResult[i,-lookahead:]
    error = eval_model(x, y)
    print('average error: %f'%(error))
    # save truth and predict results
    write_result('truth_%s_%d_%d_%d.txt'%(path, epochs, step, lookahead), testResult)
    write_result('predict_%s_%d_%d_%d_%.4f.txt'%(path, epochs, step, lookahead, error), predictResult)
    print('truth and predicted result saved')
    
if __name__ == '__main__':
    main()

