import numpy as np
import os

import keras.layers as kl
import keras.models as km

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
                print(fileName, line)
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
def build_train_set(flist, start, end, step):
    trainSet = np.zeros((end-start, step, DIM), dtype=np.int32)
    print('b')
    for i in range(start, end):
        #print(i)
        trainSet[i-start,:,:] = build_event_dataset(flist, i, i+step)
    return trainSet

# build dataset used for rnn test
def build_train_result(flist, start, end, step):
    trainResult = np.zeros((end-start, 1, DIM), dtype=np.int32)
    for i in range(start, end):
        trainResult[i-start,:,:] = build_event_dataset(flist, i+step, i+step+1)

    trainResult = np.reshape(trainResult, (end-start,DIM))    
    return trainResult

def write_result(filename, data):
    with open(filename, 'w') as f:
        for line in data:
            for e in line:
                f.write(str(e) + ' ')
            f.write('\n')

print('start')
path = 'attr'
flist = sort_file_list(path)
trainSize = 1500
testSize = 60
step = 30
# build training and test datasets
trainData = build_train_set(flist, 0, trainSize, step)
print('1')
trainResult = build_train_result(flist, 0, trainSize, step)
print('2')
testData = build_train_set(flist, trainSize, trainSize+testSize, step)
print('3')
testResult = build_train_result(flist, trainSize, trainSize+testSize, step)
print('4')

# tain model
model = km.Sequential()
model.add(kl.LSTM(DIM, input_shape=(step, DIM), activation='relu'))
#model.add(kl.LSTM(DIM, input_dim = DIM, input_length = step, activation='sigmoid'))
model.add(kl.Dense(DIM))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainData, trainResult, epochs=3000, batch_size=32, verbose=2, validation_split = 0.05)
# save model
model.save('model.h5')
# predict and evaluate
predict = model.predict(testData)
write_result('truth.txt', testResult)
write_result('predict.txt', predict)
        
errorSum = 0
for i in range(testSize):
    diff = sum(predict[i,:] - testResult[i,:]) / sum(testResult[i,:])
    errorSum = errorSum + diff * diff
errorAve = errorSum / testSize
print('average error: %f'%(errorAve))

