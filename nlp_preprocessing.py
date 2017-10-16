import os
import re
from nltk.stem import WordNetLemmatizer
#import gensim
import pickle
import numpy as np

# load a list of words, such as stop words, common words from a text file
def load_word_list(fileName):
    words = set()
    with open(fileName, 'r') as f:
        for line in f:
            words.add(line.strip('\n'))
    return words

# remove stop words, convert to lower case, remove meaningless signals
def clean_news(path, stop_word_list):
    num = 0
    stopWords = load_word_list(stop_word_list)
    
    flist = os.listdir(path)
    newPath = 'news_clean'
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    # deal with each file
    for f in flist:
        with open(os.path.join(path,f), 'r') as src:
            string = '' # will be written into target file
            line = src.readline().strip('\n')
            while line != '':
                newLine = ''
                content = line.split('\t')
                # ignore no id events
                if len(content) < 3:
                    line = src.readline().strip('\n')
                    continue

                if content[2] != '':    # ignore empty news
                    # replace tab with space
                    for i in range(3, len(content)):
                        content[2] = content[2] + ' ' + content[i]
                    # to lower case, then split and remove meaningless signals
                    words = re.split('[^a-zA-Z0-9$]', content[2].lower())
                    for word in words:
                        if (word not in stopWords) and word != '':
                            newLine = newLine + word + ' '
                    string = string + '%s\t%s\n'%(content[0], newLine)
                    num += 1
                line = src.readline().strip('\n')
        with open(os.path.join(newPath,f), 'w') as tar:
            tar.write(string)
    print('total news: %d'%(num))

# count the length distribution of news
def counter(path):
    dic = dict()
    flist = os.listdir(path)
    for f in flist:
        with open(os.path.join(path,f),'r') as fid:
            for line in fid:
                num = len(line.split(' '))
                num = int(num/1500)
                if num in dic.keys():
                    dic[num] += 1
                else:
                    dic[num] = 1
    return dic

# get the corresponding attributes (number of mentions, sentiments, etc) of each news
def matchId(srcPath, tarPath):
    flist = os.listdir(tarPath)
    newPath = 'news_match'
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    for f in flist:
        idDic = dict()
        src, tar = os.path.join(srcPath,f), os.path.join(tarPath,f)
        f1 = open(src,'r')
        f2 = open(tar,'r')
        line = f1.readline().strip('\n')
        while line != '':
            content = line.split('\t')
            idDic[content[0]] = (content[25],content[29],content[30],content[31],content[32],content[33],content[34])
            line = f1.readline().strip('\n')
        line = f2.readline().strip('\n')
        string = ''
        while line != '':
            index = line.find('\t')
            attr = idDic[line[:index]]
            string += merge(attr, line[index+1:])
            line = f2.readline().strip('\n')
        out = open(os.path.join(newPath,f),'w')
        out.write(string)
        f1.close(), f2.close(), out.close()
def merge(attr, line):
    s = ''
    for e in attr:
        s = s + e + '\t'
    s = s + line + '\n'
    return s

# average the attributes of duplicated news
def attr_ave(path):
    newPath = 'news_ave'
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    flist = os.listdir(path)
    for f in flist:
        attrs = dict()
        news, newsSet = list(), set()
        string = ''
        with open(os.path.join(path,f),'r') as src:
            for line in src:
                upgradeAttr(news, attrs, line)
        for e in news:
            key = e[30:60]
            if key not in newsSet:
                string = string + attr_to_str(attrs[key]) + e + '\n'
                newsSet.add(key)
        # write the average results
        with open(os.path.join(newPath,f),'w') as tar:
            tar.write(string)

# upgrade the attributes of a news when reading a new line
def upgradeAttr(news, attrs, line):
    content = line.strip('\n').split('\t')
    news.append(content[7])
    key = content[7][30:60]
    item = [1]
    item.extend(content[0:7])
    for i in range(len(item)):
        try:    # none
            item[i] = float(item[i])
        except:
            item[i] = 0
    if key in attrs.keys():
        for i in range(len(item)):
            attrs[key][i] += item[i]
    else:
        attrs[key] = item

# convert a series attributes to a string
def attr_to_str(attr):
    l = list()
    num = int(attr[0])
    # compute average
    for i in range(1, len(attr)):
        l.append(float(attr[i])/num)
    # convert to string
    string = ''
    for e in l:
        string = string + str(round(e,2)) + '\t'
    return string

# join all file and generate a single file
def join_files(path, newFile):
    flist = os.listdir(path)
    num = 0
    string = ''
    with open(newFile, 'w') as tar:
        for f in flist:
            with open(os.path.join(path,f),'r') as src:
                line = src.readline().strip('\n')
                while line != '':
                    num += 1
                    string = string + line + '\n'
                    if num%500 == 0:
                        print(num)
                        tar.write(string)
                        string = ''
                    line = src.readline().strip('\n')
        if string != '':
            tar.write(string)

# stem, split joint numbers and letters, remove single letter, remove :aren, haven ...
def stem_words(newsdata, stop_word_list):
    stopWords = load_word_list(stop_word_list)

    target = 'news_stem'
    with open(newsdata, 'r') as src:
        with open(target, 'w') as tar:
            for line in src:
                temp = line.strip('\n').strip(' ')
                index = temp.rfind('\t')
                content = split_num_letter(temp[index+1:])
                newLine = stem_single_stop(content, stopWords)
                tar.write('%s\t%s\n'%(temp[:index], newLine))

def split_num_letter(line):
    string = ''
    pre = 0 # 0: space(asic 32), 1: letter, 2: number, 3: other
    for e in line:
        if ord(e) == 32:
            pre = 0
            string += e
        elif ord(e) > 96 and ord(e) < 123:
            if pre == 0 or pre == 1:
                string += e
            else:
                string = string + ' ' + e
            pre = 1
        elif ord(e) > 47 and ord(e) < 58:
            if pre == 0 or pre == 2:
                string += e
            else:
                string = string + ' ' + e
            pre = 2
        else:
            if pre == 0:
                string += e
            else:
                string = string + ' ' + e
            pre = 3
    return string
def stem_single_stop(content, stopWords):
    string = ''
    wnl = WordNetLemmatizer()
    for word in content.split(' '):
        if word == '$':
            string += 'dollar '
        elif len(word) > 1 and (word not in stopWords):
            word = wnl.lemmatize(word)
            if word not in stopWords:
                string = string + word + ' '
    return string

# split files into batches
def generate_batch_file(fileName, limit):
    num = -1
    index = 0
    src = open(fileName, 'r')
    tar = open('%s_%d'%(fileName, index), 'w')
    line = src.readline()
    while line != '':
        num += 1
        if num != 0 and num%limit == 0:
            tar.close()
            index += 1
            tar = open('%s_%d'%(fileName, index), 'w')
        tar.write(line)
        line = src.readline()
    tar.close()

# store vocab and weights into binary files
def build_vocab_weights(commonWordFile, w2vFile):
    commonWords = set()
    length = 0
    dim = 50
    # load common words and compute number of words
    with open(commonWordFile, 'r') as src:
        for line in src:
            commonWords.add(line.strip('\n'))
            length += 1
    index = 1
    vocab = dict()
    weights = np.zeros((length+1, dim), dtype=np.float32)    # {index: [vector], ...}
    model = gensim.models.KeyedVectors.load_word2vec_format(w2vFile, binary=False)
    # generate weights only for common words
    for word in commonWords:
        try:
            weights[index] = model[word]
            vocab[word] = index
            index += 1
        except:
            print(word)
    sums = 0
    for i in range(index, length+1):
        sums += sum(weights[i])
    if sums == 0:
        print('yes')
        weights = weights[:index]
    else:
        print(sums)
        
    print(len(vocab), length)
    # store into binary files
    with open('vocab_%d_%s.pkl'%(index-1,dim),'wb') as handle:
        pickle.dump(vocab, handle)
    np.save('weights_%d_%s.npy'%(index-1,dim), weights)
    return vocab, weights

# extract data from one line of text, require strip(' ') first
# return np arrays
def extract_data(line, vocab, commonWords):
    content = line.split('\t')
    result = compute_result(content[:-1])
    source = content[-1]
    data = []
    for word in source.split(' '):
        if word not in commonWords:
            try:
                data.append(vocab[word])
            except:
                pass
                #data.append(vocab['unk'])
    # make every input have same length
    data = padding(data)
    return np.array(data), np.array(result)

# compute results based on the attributes
def compute_result(attrs):
    # attrs: isroot, quadclass, glodstein, mentions, sources, articles, tone
    return round((float(attrs[3]) + float(attrs[5]))*float(attrs[6])/2, 2)

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
# extract input data and results from a file
def build_dataset(fileName, vocab, commonWords):
    trainData, trainResult = [], []
    with open(fileName, 'r') as src:
        line = src.readline().strip('\n')
        while line != '':
            # extract data and result from each line
            data, result = extract_data(line.strip(' '), vocab, commonWords)
            trainData.append(data)
            trainResult.append(result)
            line = src.readline().strip('\n')
    return trainData, trainResult

# build train data and results (numpy binary) for batches
def build_batch_data(path, vocabFile, commonWordsFile):
    commonWords = load_word_list(commonWordsFile)
    with open(vocabFile, 'rb') as handle:
        vocab = pickle.load(handle)
    flist = os.listdir(path)
    for f in flist:
        fileName = os.path.join(path,f)
        tx, ty = build_dataset(fileName, vocab, commonWords)
        np.save(f+'_x.npy', np.array(tx, dtype=np.int32))
        np.save(f+'_y.npy', np.array(ty, dtype=np.float32))
        
#clean_news('news_201304', 'stop_words2.txt')
#matchId('201304now','news_clean')
#attr_ave('news_match')
#stem_words('news_data', 'stop_words_clean.txt')
#build_vocab_weights('common_words_8299.txt', 'glove50_gensim.txt')
#generate_batch_file('news_stem',50)
build_batch_data('news_50', 'vocab_glove50.pkl', 'common_words_1k.txt')
