from nltk.stem import WordNetLemmatizer
import os
'''
import rnn_model as rm
import keras

lookahead = 5
path = 'attr-us'
trainData, trainResult, testData, testResult = rm.build_datasets(path, lookahead=lookahead)
model = keras.models.load_model('__data__/model-us2.h5')
error = rm.eval_model_ahead(model, testData, testResult, lookahead)
'''

'''
# search a spcific line
f = open('temp/20170515.export.CSV','r')
eid = '655626863'
f2 = open(eid,'w')
for l in f:
    c = l.split('\t')
    if c[0] == eid:
        for e in c:
            f2.write(e + '\n')

f.close()
f2.close()
'''

# check whether non-letters
def check(fileName):
    n = 0
    flag = False
    with open(fileName,'r') as src:
        for line in src:
            #content = re.split('[^a-z]', line.strip('\n').lower())
            for e in line.strip('\n'):
                if ord(e) < 97 or ord(e) > 122:
                    flag = True
            if flag:
                #print(line)
                n += 1
                flag = False
    print(n)
# to lower
def clean_common_words(fileName):
    target = 'common_words_clean.txt'
    with open(fileName,'r') as src:
        with open(target, 'w') as tar:
            for line in src:
                tar.write(line.lower())
# stem and remove stop words
def stem_words(fileName):
    common_words = set()
    stop_word_list = 'stop_words_clean.txt'
    stopWords = set()
    with open(stop_word_list, 'r') as f:
        for line in f:
            stopWords.add(line.strip('\n'))
    wnl = WordNetLemmatizer()
    with open(fileName, 'r') as src:
        for line in src:
            word = line.strip('\n')
            if word not in stopWords:
                word = wnl.lemmatize(word)
                if word not in stopWords:
                    common_words.add(word)
    target = 'common_words_stem.txt'
    with open(target, 'w') as tar:
        for word in common_words:
            tar.write(word + '\n')

def search_url(number):
    fileName = '20160915.export.CSV'
    with open(fileName, 'r') as src:
        for line in src:
            c = line.strip('\n').split('\t')
            if c[0] == number:
                return c[57]

# note: whether space after each line
def build_corpus(path):
    flist = os.listdir(path)
    with open('corpus.txt', 'w') as tar:
        for f in flist:
            string = ''
            with open(os.path.join(path,f), 'r') as src:
                line = src.readline().strip('\n')
                while line != '':
                    string = string + line.split('\t')[-1] + ' '
                    line = src.readline().strip('\n')
                tar.write(string)

def isNum(c):
    if ord(c) > 47 and ord(c) < 58:
        return True
    else:
        return False
def num_to_word(num):
    if num < 10:
        return 'several'
    elif num < 100:
        return 'ten'
    elif num < 1000:
        return 'hundred'
    elif num < 10000:
        return 'thousand'
    elif num < 5000000:
        return 'million'
    elif num < 5000000000:
        return 'billion'
    else:
        return 'huge amount'
def convert_num(path):
    newPath = 'news_50_num'
    flist = os.listdir(path)
    for f in flist:
        string = ''
        with open(os.path.join(path,f), 'r') as src:
            line = src.readline().strip('\n')
            while line != '':
                index = line.rfind('\t')
                string = string + line[:index] + '\t'
                content = line[index+1:].strip(' ')
                temp = ''
                for i in range(len(content)):   # remove space between numbers
                    if content[i] != ' ':
                        temp += content[i]
                    elif (not isNum(content[i-1])) or (not isNum(content[i+1])):
                        temp += content[i]
                for e in temp.split(' '):
                    if isNum(e[0]):
                        string = string + num_to_word(int(e)) + ' '
                    else:
                        string = string + e + ' '
                string = string.strip(' ')
                string = string + '\n'
                line = src.readline().strip('\n')
        with open(os.path.join(newPath,f), 'w') as tar:
            tar.write(string)
#split_file('tmp',4)
#check('common_words2.txt')
#clean_common_words('common_words.txt')
#stem_words('common_words2.txt')
build_corpus('news_50_num/')
#convert_num('__data__/news_50/')
