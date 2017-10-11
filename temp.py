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

def split_file(fileName, limit):
    num = 0
    index = 0
    src = open(fileName, 'r')
    tar = open('%s_%d'%(fileName, index), 'w')
    line = src.readline()
    while line != '':
        num += 1
        if num%limit == 0:
            tar.close()
            index += 1
            tar = open('%s_%d'%(fileName, index), 'w')
        tar.write(line)
        line = src.readline()
    tar.close()
split_file('tmp',4)
