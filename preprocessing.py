import os
import logger
'''
    This file contains a set of functions that are helpful for cleaning data and copy designated data
    into the new files
'''
logpath='cleaning.log'
fid = open(logpath, 'w') #create empty log file
fid.close()

'''
    this function is used for extracting the events that are satisfied with the set value of specified column
    parameters:
        fname: the name of readed file
        oname: the name of writed file
        col: the index of the column
        value: the value of colnum
        writerpath: the path of the directory of cleaned data
        @return line_count:the count of copied lines
'''

def get_specified_data(path, countryColumn, country, attrColumn):
    newpath = 'attr_' + country + '_' + path
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    flist = os.listdir(path)  # all files in the directory
    for f in flist:
        count = 0
        fname, newfname = path+f, newpath+f
        dictionary = {} # store how many times each attributes occures
        reader=open(fname,'r',encoding='utf-8')
        writer=open(newfname,'w',encoding='utf-8')
        for line in reader:
            columns = line.strip('\n').split('\t')
            for i in countryColumn:
                if columns[i] == country: # match country
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
        logger.log('attr processing of ' + fname + ' finished',logpath) # log info after each file is processed
    return newpath

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
                if i not in idxs:
                    string = string + items[i]+'\t'
            writer.write(string+'\n')
        writer.close()
        reader.close()
        logger.log('delete ' + fname + ' finished',logpath) # log info after each file is processed
    return newpath

