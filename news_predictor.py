import re
import pickle

import numpy as np
import keras.models as km

import nlp_preprocessing as pre

# extract data from one line of text
# return np arrays
def extract_data(source, vocab):
    data = []
    for word in source.split(' '):
        try:
            data.append(vocab[word])
        except:
            pass
            #data.append(vocab['unk'])
    # make every input have same length
    data = padding(data)
    return np.array(data)

# padding zeros
def padding(data):
    LEN = 500
    length = len(data)
    if length < LEN:
        for i in range(length,LEN):
            data.append(0)
    elif length > LEN:
        data = data[:LEN]
    return data

###############################################################################################

string = 'require the raw news, no need of preprocessing $100 399km ^* is the'  # require the raw news, no need of preprocessing
w2vFile = 'glove50'
vocabFile = 'vocab_%s.pkl'%(w2vFile)
weightsfile = 'weights_%s.npy'%(w2vFile)
stop_word_list = 'stop_words2.txt'
modelFile = 'hot_news_predict.h5'

# load predict model
model = km.load_model(modelFile)

# load vocabulary used for word indexing
with open(vocabFile, 'rb') as handle:
    vocab = pickle.load(handle)

# load stop word list
stopWords = set()
with open(stop_word_list, 'r') as f:
    for line in f:
        stopWords.add(line.strip('\n'))

# remove stop words and meaningless signals
content = re.split('[^a-zA-Z0-9$]', string.lower())
words = ''
for e in content:
    if e != '' and (e not in stopWords):
        words = words + e + ' '

# split letters, numbers and signals
words = pre.split_num_letter(words)
# stem words
words = pre.stem_single_stop(words, stopWords)

# indexing, convert text to vector
data = extract_data(words.strip(' '), vocab)
predict = model.predict(np.array([data]))
result = predict[0][0]
#print(result, words)
