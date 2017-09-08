#coding=utf-8
def del_cvs_col(fname,newfname,idxs):
    with open(fname) as reader, open(newfname, 'w') as writer:
        for line in reader:
            items = line.strip().split(',')
            string =[]
            for i in range(0,len(items)):
                if i not in idxs:
                   string.append(items[i])
            #print(string)
            print(','.join(string), file=writer)

