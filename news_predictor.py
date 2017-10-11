import re
import pickle

import numpy as np
import keras.models as km

# extract data from one line of text
# return np arrays
def extract_data(source, vocab):
    data = []
    for word in source.split(' '):
        try:
            data.append(vocab[word])
        except:
            data.append(vocab['unk'])
    # make every input have same length
    data = padding(data)
    return np.array(data)

# padding zeros
def padding(data):
    LEN = 1500
    length = len(data)
    if length < LEN:
        for i in range(length,LEN):
            data.append(0)
    elif length > LEN:
        data = data[:LEN]
    return data

string  # require the raw news, no need of preprocessing
vocab_file = 'vocab_glove50.pkl'
stop_word_list = 'stop_words2.txt'
model_file = 'hot_news_predict.h5'

# load predict model
model = keras.load_model(model_file)

# load vocabulary used for word indexing
with open(vocab_file, 'rb') as handle:
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
    if e != '' and (word not in stopWords):
        words = words + e + ' '

# indexing, convert text to vector
data = extract_data(words.strip(' '), vocab)
prdict = model.predict(np.array([data]))

