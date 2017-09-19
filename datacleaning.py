import logger
'''
    This file contains a set of functions that are helpful for cleaning data and copy designated data
    into the new files
'''
logpath='cleaning.log'

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

def get_specified_data(fname,oname,col,value,count):
    line_count=0
    reader=open(fname,'r',encoding='utf-8')
    writer=open(oname,'a',encoding='utf-8')
    for line in reader:
        columns=line.split('\t')
        for i in col:
            if columns[i]==value:
                writer.write(line)
        line_count+=1
    reader.close()
    writer.close()
    logger.log(str(fname+''+'currentcount is:'+str(count)),logpath)
    return line_count

'''
    function for extracting the events happened in the wanted countries
    parameter:
        fname: the name of the file that iftoberead
        newfname: the name of output file
        idxs: the columns that should be excluded in the output files
        @return line_count
'''

def del_cvs_col(fname,newfname,idxs,count):
    line_count=0
    reader=open(fname,'r',encoding='utf-8')
    writer=open(newfname,'a',encoding='utf-8')
    for line in reader:
        items=line.split('\t')
        string=''
        for i in range(0,len(items)):
            if i not in idxs:
                string = string + items[i]+'\t'
        writer.write(string+'\n')
        line_count+=1
    writer.close()
    reader.close()
    logger.log(str(fname+''+'currentcount is:'+str(count)),logpath)
    return line_count