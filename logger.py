def log(str, logpath):
	with open(logpath, 'a', encoding='utf-8') as logfile:
		logfile.write(str+'\n')
		logfile.close()