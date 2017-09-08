import os
count = 0
flist = os.listdir('../extracted')
for f in flist:
        logger = open('cleaning1.log','a',encoding='utf-8')
        tmp = f.split('.')[0]
        thisyear = tmp[0:4]
        input = open('../extracted/'+f,'r',encoding='utf-8')
        output = open('../ausdata1/'+thisyear+'.csv','a',encoding='utf-8')
        for line in input:
                coloumns = line.split('\t')
                if coloumns[7] == 'AUS' or coloumns[15] == 'AUS' or coloumns[17] == 'AUS' or coloumns[51] == 'AS':
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