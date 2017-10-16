import os
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dropout, Dense 
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
import keras.optimizers as opt
#import gensim

LEN = 750  # the input length

# index and embed raw text
def gen_embed_model(modelFile):
    vocab = {}  # {'word': index, ...}
    with open(modelFile, 'r') as f:
        line = f.readline()
        [length, dim] = line.split(' ')
        vec = np.zeros((int(length)+1, int(dim)), dtype = np.float64)    # {index: [vector], ...}
        line = f.readline()
        i = 1
        while line != '':
            index = line.find(' ')
            word = line[:index]
            vector = []
            for e in line[index+1:].split(' '):
                try:
                    vector.append(float(e))
                except Exception:
                    print('float' + e)
            vocab[word] = i
            vec[i] = np.array(vector)
            line = f.readline()
            i = i+1
    return vocab, vec

# extract data from one line of text, require strip(' ') first
# return np arrays
def extract_data(line, model):
    content = line.split('\t')
    result = compute_result(content[:-1])
    source = content[-1]
    data = []
    for word in source.split(' '):
        try:
            data.append(model[word])
        except:
            pass
            #data.append(model['unk'])
    # make every input have same length
    data = padding(data)
    return np.array(data), np.array(result)

# compute results based on the attributes
def compute_result(attrs):
    # attrs: isroot, quadclass, glodstein, mentions, sources, articles, tone
    return round((float(attrs[3]) + float(attrs[5]))*float(attrs[6])/2, 2)

# padding zeros
def padding(data):
    length = len(data)
    if length < LEN:
        for i in range(length,LEN):
            data.append(0)
    elif length > LEN:
        data = data[:LEN]
    return data

# generate datasets used for training and testing
def gen_datasets(path, vocab):
    trainData, trainResult = [], []
    num = 0
    with open(path ,'r') as src:
        line = src.readline().strip('\n')
        while line != '':
            num += 1
            # remove trail line feed and white space
            data, result = extract_data(line.strip(' '), vocab)
            trainData.append(data)
            trainResult.append(result)
            line = src.readline().strip('\n')
    testData, testResult = trainData[-500:], trainResult[-500:]
    trainData = trainData[:-500]
    trainResult = trainResult[:-500]
    return np.array(trainData, dtype=np.int32), np.array(trainResult, dtype=np.float32), np.array(testData, dtype=np.int32), np.array(testResult, dtype=np.float32)

# extract input data and results from a file
def build_dataset(fileName, vocab):
    trainData, trainResult = [], []
    with open(fileName, 'r') as src:
        line = src.readline().strip('\n')
        while line != '':
            # extract data and result from each line
            data, result = extract_data(line.strip(' '), vocab)
            trainData.append(data)
            trainResult.append(result)
            line = src.readline().strip('\n')
    return trainData, trainResult

# a generator used to fit the rnn model
def train_data_generator(dataPath, limit, vocab):
    total = 2528
    index = 0
    while True:
        inputs, targets = build_dataset('%s%d'%(dataPath, index), vocab)
        for i in range(1, limit):
            index += 1
            if index == total:
                index = 0
            newInputs, newTargets = build_dataset('%s%d'%(dataPath, index), vocab)
            inputs.extend(newInputs)
            targets.extend(newTargets)
        if index%50 == 0:
            print(index)
        yield (np.array(inputs, dtype=np.int32), np.array(targets, dtype=np.float32))
        index += 1
        if index == total:
            index = 0
def train_data_generator2(dataPath):
    total = 2528
    index = 0
    while True:
        inputs = np.load('%s%d%s'%(dataPath, index, '_x.npy'))
        targets = np.load('%s%d%s'%(dataPath, index, '_y.npy'))
        if index%50 == 0:
            print(index)
        yield inputs, targets
        index += 1
        if index == total:
            index = 0
'''
path = 'news_ave'
w2vfile = 'glove50_gensim.txt'
#trainData, trainResult, testData, testResult = gen_datasets(path, w2vfile)
vocab, embedModel = gen_embed_model(w2vfile)   # vocab: {word: index, ...} embedModel: np array
with open('vocab_glove50.pkl','wb') as handle:
    pickle.dump(vocab, handle)
np.save('w2v_weights_glove50.npy',embedModel)
'''
'''
with open('vocab_8229_50.pkl', 'rb') as handle:
    vocab = pickle.load(handle)


path = 'newsdata_64/news_data_0'
w2vfile = 'glove50_gensim.txt'
#trainData, trainResult, testData, testResult = gen_datasets(path, vocab)
'''
embedModel = np.load()
# build and fit model
model = Sequential()
model.add(Embedding(400001,50, input_length=LEN, mask_zero=True,weights=[embedModel]))
model.add(LSTM(50,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(20,activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))
#sgd = opt.SGD(lr=0.1, decay=1e-2, momentum=0.9)
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit_generator(train_data_generator2('news_50_bin/news_stem_'), 500, epochs=10, verbose=2, validation_data=None)
#model.fit(trainData, trainResult, epochs=10, batch_size=30, verbose=2, validation_split = 0.05)
model.save('text.h5')

'''
# create the model
model = Sequential()
model.add(Embedding(400001, 50, input_length=LEN, mask_zero=False,weights=[embedModel]))
model.add(Conv1D(filters=32, kernel_size=20, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(trainData, trainResult, epochs=20, batch_size=60, verbose=2, validation_split = 0.05)
'''


