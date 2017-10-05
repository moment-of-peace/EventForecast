import numpy as np
import os

import keras.layers as kl
import keras.models as km

DIM = 20

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
            line = f.readline().strip('\n')
    return vec

# build a raw dataset containing a series of event type distribution
def build_event_dataset(path, start=0, end=None):
    flist = os.listdir(path)  # all files in the directory
    dataset = np.zeros((end-start, DIM), dtype=np.int32)
    if end == None:
        end = len(flist)
    for i in range(start, end):
        dataset[i-start,:] = build_event_vec(os.path.join(path,flist[i]))
    return dataset

# build dataset used for rnn training
def build_train_set(path, start, end, step):
    trainSet = np.zeros((end-start, step, DIM), dtype=np.int32)
    for i in range(start, end):
        trainSet[i-start,:,:] = build_event_dataset(path, i, i+step)
    return trainSet

# build dataset used for rnn test
def build_train_result(path, start, end, step):
    trainResult = np.zeros((end-start, 1, DIM), dtype=np.int32)
    for i in range(start, end):
        trainResult[i-start,:,:] = build_event_dataset(path, i+step, i+step+1)

    trainResult = np.reshape(trainResult, (end-start,DIM))    
    return trainResult

path = 'attr'
trainSize = 1500
testSize = 60
step = 30
# build training and test datasets
trainData = build_train_set(path, 0, trainSize, step)
trainResult = build_train_result(path, 0, trainSize, step)
testData = build_train_set(path, trainSize, trainSize+testSize, step)
testResult = build_train_result(path, trainSize, trainSize+testSize, step)
# tain model
model = km.Sequential()
model.add(kl.LSTM(DIM, input_shape=(DIM, step), activation='sigmoid'))
model.add(kl.Dense(DIM))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainData, trainResult, epochs=500, batch_size=10, verbose=1)
# predict and evaluate
predict = model.predict(testData)
errorSum = 0
for i in range(testSize):
    diff = sum(predict[i,:] - testResult[i,:]) / sum(testResult[i,:])
    errorSum = errorSum + diff * diff
errorAve = errorSum / testSize
print('average error: %f'%(errorAve))

