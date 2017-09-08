'''
    This file cleans the data according to the set colomns' value
    The different data will be copied into different files
    it contains several functions that are useful
'''
#coding=utf-8

import os
count = 0
flist = os.listdir('../extracted')

col = [36]
content = 'Australia'

for f in flist:
    logger = open('cleaning1.log','a',encoding='utf-8')
    tmp = f.split('.')[0]
    thisyear = tmp[0:4]
    input = open('../extracted/'+f,'r',encoding='utf-8')
    output = open('../ausdata1/'+thisyear+'.csv','a',encoding='utf-8')
    for line in input:
        columns = line.split('\t')
        for i in col:
            if columns[i] == content:
                output.write(line)
                count += 1
                
    output.close()
    input.close()
    logger.write(f+'  ')
    logger.write('current count is:'+str(count)+'\n')
    logger.close()
logger = open('cleaning.log','a',encoding='utf-8')
logger.write('final count is:'+str(count))
logger.close()
'''
    function for removing the url
'''

