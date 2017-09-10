import datacleaning
import os
import logger
data_cleaning_logpath = 'cleaning.log'
flist = os.listdir('datafiles/201304now/')
count = 0
count1 = 0
for f in flist:
    tmp_count = datacleaning.del_cvs_col('datafiles/201304now/'+f,'cleaned/2013/'+f,[57],count1)
    count1 = tmp_count

flist1 = os.listdir('cleaned/2013/')
for f1 in flist1:
	tmp_count = datacleaning.get_specified_data('datafiles/2013/'+f1,'filtered/2013/ausdata.csv',[36],'Australia',count)
	count = tmp_count
	
logger.log('final count is:' + str(count),data_cleaning_logpath)
logger.log('final count is:' + str(count1),data_cleaning_logpath)