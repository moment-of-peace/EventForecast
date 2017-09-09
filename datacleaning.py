import logger
'''
    Thisfilecontainsasetoffunctionsthatishelpfulforcleaningdataandcopydesignateddata
    intothenewfiles
'''
logpath='cleaning.log'

'''
    thisfunctionisusedforextractingtheeventsthataresatisfiedwiththesetvalueofspecifiedcolumn
    parameters:
        fname:thenameofreadedfile
        oname:thenameofwritedfile
        col:theindexofthecolumn
        value:thevalueofcolnum
        writerpath:thepathofthedirectoryofcleaneddata
        @returnline_count:thecountofcopiedlines
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
    functionforextractingtheeventshappenedinthewantedcountries
    parameter:
        fname:thenameofthefilethatiftoberead
        newfname:thenameofoutputfile
        idxs:thecolumnsthatshouldbeexcludedintheoutputfiles
        @returnline_count
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