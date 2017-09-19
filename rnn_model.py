import numpy as np
import os

import keras.layers as kl
import rnn_model as rnn


# build a vector to represent the event type distibution
def build_event_vec(fileName):
    vec = np.zeros(20, dtype=np.int32)
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
    dataset = np.zeros((end-start, 20), dtype=np.int32)
    if end == None:
        end = len(flist)
    for i in range(start, end):
        dataset[i-start,:] = build_event_vec(os.path.join(path,flist[i]))
    return dataset

# build dataset used for rnn training
def build_train_set(path, size, step):
    dim = 20
    trainSet = np.zeros((size, step, dim), dtype=np.int32)
    for i in range(size):
        trainSet[i,:,:] = build_event_dataset(path, i, i+step)
    return trainSet

# build dataset used for rnn test
def build_train_result(path, size, step):
    dim = 20
    trainSet = np.zeros((size, 1, dim), dtype=np.int32)
    for i in range(size):
        trainSet[i,:,:] = build_event_dataset(path, i+step, i+step+1)
    return trainSet

path = 'attr'
trainData = build_train_set(path, 1500, 30)
trainResult = build_train_result('attr', 1500, 30)

model = km.Sequential()
model.add(kl.LSTM(20, input_shape=(30,20), activation='sigmoid'))
model.add(kl.Dense(20))
model.compile(loss='mean_squared_error', optimizer='adam')
trainResult = np.reshape(trainResult, (1500,20))
model.fit(trainData, trainResult, epochs=100, batch_size=10, verbose=2)

