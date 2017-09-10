import datetime
def log(s, logpath):
	with open(logpath, 'a', encoding='utf-8') as logfile:
		logfile.write(s+' '+str(datetime.datetime.now())+'\n')
		# if use with...as, don't need logfile.close()
