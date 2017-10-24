import os
from urllib.parse import urlparse
import operator

'''
    This file contains a set of functions that are used for data cleaning and extraction
'''
logpath='cleaning.log'
fid = open(logpath, 'w') #create empty log file
fid.close()

'''
    this function is used for extracting the events in a specified country
    
'''

def get_specified_data(path, countryColumn, country, attrColumn):
    newpath = path + '_attr'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    flist = os.listdir(path)  # all files in the directory
    for f in flist:
        count = 0
        fname, newfname = os.path.join(path,f), os.path.join(newpath,f)
        dictionary = {} # store how many times each attributes occures
        reader=open(fname,'r',encoding='utf-8')
        writer=open(newfname,'w',encoding='utf-8')
        for line in reader:
            columns = line.strip('\n').split('\t')
            for i in countryColumn:
                # have bug
                #if columns[i] == country: # match country
                if country in columns[i]:
                    count = count + 1
                    key = columns[attrColumn][:2] # for a event code, say 042, we just need 04
                    if key in dictionary.keys():
                        dictionary[key] = dictionary[key]+1
                    else:
                        dictionary[key] = 1;
        writer.write(country+'\n')
        dict_writer(writer, dictionary) # write the dictionary to a file
        writer.close()
        reader.close()
        log('attr processing of ' + fname + ' finished',logpath) # log info after each file is processed
    return newpath

# write a dictionary to a file
def dict_writer(writer, dictionary):
    for key, value in dictionary.items():
        writer.write(key + ': ' + str(value) + '\n')

'''
    function for extracting the events happened in the wanted countries
    parameter:
        fname: the name of the file that iftoberead
        newfname: the name of output file
        idxs: the columns that should be excluded in the output files
        @return line_count
'''
def url_columns(path, idxs):
    log('start to get urls', logpath)
    urldic = {}
    newpath= 'url_' + path
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    flist = os.listdir(path)  # all files in the directory
    for f in flist:
        fname, newfname = path+f, newpath+f
        reader=open(fname,'r',encoding='utf-8')
        writer=open(newfname,'w',encoding='utf-8')
        for line in reader:
            items=line.strip('\n').split('\t')
            try:
                if 'Australia' not in items[36] or 'Australia' not in items[43]:
                    continue
            except Exception as e:
                log(str(line)+'  error', logpath)
                log(str(e), logpath)
            string=''
            for i in range(0,len(items)):
                if i in idxs:
                    # process url
                    if i == 57:
                        r = urlparse(items[i])
                        string = string + str(r.scheme)+'://'+str(r.hostname)+'\t'+items[i]
                        key = str(r.hostname)
                        if key in urldic.keys():
                            urldic[key] = urldic[key]+1
                        else:
                            urldic[key] = 1;
                    else:
                        string = string + items[i]+'\t'
            writer.write(string+'\n')
        writer.close()
        reader.close()
        log('delete ' + fname + ' finished',logpath) # log info after each file is processed
        
    sortBKs = sorted(urldic.items(),key=lambda t:t[1]) 
    for key, value in sortBKs:
        with open('urllist.txt','a',encoding='utf-8') as uf:
            uf.write(key + '\t' + str(value) + '\n')
    log('finish get urls', logpath)
    return newpath


'''
    used for cleaning useless columns
'''
def del_columns(path, idxs):
    newpath= 'del_' + path
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    flist = os.listdir(path)  # all files in the directory
    for f in flist:
        fname, newfname = path+f, newpath+f
        reader=open(fname,'r',encoding='utf-8')
        writer=open(newfname,'w',encoding='utf-8')
        for line in reader:
            items=line.strip('\n').split('\t')
            string=''
            for i in range(0,len(items)):
                if i in idxs:
                    string = string + items[i]+'\t'
            writer.write(string+'\n')
        writer.close()
        reader.close()
        log('delete ' + fname + ' finished',logpath) # log info after each file is processed
    return newpath

'''
    used to record the processing progress
'''
def log(s, logpath):
	with open(logpath, 'a', encoding='utf-8') as logfile:
		logfile.write(s+' '+str(datetime.datetime.now())+'\n')

columns = [1,7,17,25,26,29,30,31,32,33,34,35,36,42,43,53,54]

#clean_file_path = del_columns('data-2013/', columns)
#print('cleaned file path: ' + clean_file_path)

# notice: after delete, column index of a attr will change !
#attr_path = get_specified_data(clean_file_path,[12],'Australia',4)
