import datacleaning
import os
import logger
data_cleaning_logpath = 'cleaning.log'
flist = os.listdir('datafiles/')
count = 0
count1 = 0
for f in flist:
    tmp_count = datacleaning.get_specified_data('datafiles/'+f,'filtered/ausdata.csv',[36],'Australia',count)
    count = tmp_count
    tmp_count = datacleaning.del_cvs_col('datafiles/'+f,'cleaned/'+f,[57],count1)
    count1 = tmp_count
logger.log('final count is:' + str(count),data_cleaning_logpath)
logger.log('final count is:' + str(count1),data_cleaning_logpath)