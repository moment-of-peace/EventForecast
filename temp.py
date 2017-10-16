from nltk.stem import WordNetLemmatizer
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

#split_file('tmp',4)
#check('common_words2.txt')
#clean_common_words('common_words.txt')
#stem_words('common_words2.txt')
