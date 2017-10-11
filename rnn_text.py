import os
import pickle

import numpy as np
import keras.layers as kl
import keras.models as km
import gensim

LEN = 1500  # the input length

# index and embed raw text
def gen_embed_model(modelFile):
    vocab = {}  # {'word': index, ...}
    with open(modelFile,'r') as f:
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

# extract data from one line of text
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
            data.append(model['unk'])
    # make every input have same length
    data = padding(data)
    return np.array(data), np.array(result)

# compute results based on the attributes
def compute_result(attrs):
    # attrs: isroot, quadclass, glodstein, mentions, sources, articles, tone
    return round((float(attrs[3]) + float(attrs[5]))/2, 2)

# padding zeros
def padding(data):
    length = len(data)
    if length < LEN:
        shape = data[0].shape
        for i in range(length,LEN):
            data.append(np.zeros(shape))
    elif length > LEN:
        data = data[:LEN]
    return data

# generate datasets used for training and testing
# extract_data changed !
def gen_datasets(path, w2vfile):
    w2vModel = gensim.models.KeyedVectors.load_word2vec_format(w2vfile, binary=False)
    trainData, trainResult = [], []
    flist = os.listdir(path)
    num = 0
    for f in flist:
        with open(os.path.join(path,f) ,'r') as src:
            for line in src:
                num += 1
                if num%100 == 0:
                    print(num)
                # remove trail line feed and white space
                data, result = extract_data(line.strip('\n').strip(' '), w2vModel)
                trainData.append(data)
                trainResult.append(result)
    testData, testResult = np.array(trainData[-1000:]), np.array(trainResult[-1000:])
    trainData = np.array(trainData[:-1000])
    trainResult = np.array(trainResult[:-1000])
    return trainData, trainResult, testData, testResult

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
    return np.array(trainData), np.array(trainResult)

# a generator used to fit the rnn model
def train_data_generator(dataPath, limit, vocab):
    index = 0
    while True:
        inputs, targets = build_dataset('%s%d'%(dataPath, index), vocab)
        yield (inputs, targets)
        index += 1
        if index == limit:
            index = 0
'''
path = 'news_ave'
w2vfile = 'glove100_gensim.txt'
#trainData, trainResult, testData, testResult = gen_datasets(path, w2vfile)
vocab, embedModel = gen_embed_model(w2vfile)   # vocab: {word: index, ...} embedModel: np array
'''

'''
with open('vocab_glove100.pickle', 'rb') as handle:
    vocab = pickle.load(handle)
embedModel = np.load('w2v_weights_glove100.npy')
'''
'''
# build and fit model
model = km.Sequential()
model.add(kl.Embedding(400001,100, mask_zero=True,weights=[embedModel]))
model.add(kl.LSTM(30,activation='relu'))
model.add(kl.Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit_generator(train_data_generator('newsdata_64/news_data_', 63, vocab), 63, epochs=2000, verbose=2, validation_data=None)
'''
