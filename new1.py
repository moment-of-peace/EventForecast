import os
import treeNode as tr
def day_item(fname,event_id):
    day_event=[]
    reader=open(path+fname,'r',encoding='utf-8')
    #writer=open(newpath+fname,'w')
    list=[]
    for line in reader:
        columns=line.strip('\n').split('\t')
        if len(list)>10:#source data so long, cause memory error
            break
        if columns[event_id] not in list:
            list.append(columns[event_id])
            #writer.write(columns[event_id]+',')
    #writer.write('\n')
    #writer.close()
    reader.close()
    return list	

def read(path,event_id):
    monthDat=[]
    flist=os.listdir(path)
    #writer=open(newpath+'input_data','w')
    
    for f in flist:
        list=day_item(f,event_id)
        monthDat.append(list)
    return monthDat

def write(data,newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    writer=open(newpath+'input_data.csv','w')
    for l in data:
        for item in l:
            writer.write(item+',')
        writer.write('\n')
    writer.close()

event_id=4
path='C:\\Users\\12444\\Documents\\study\\master2\\dataMining\\project\\data_mining_five_day\\'		
newpath='C:\\Users\\12444\\Documents\\study\\master2\\dataMining\\project\\eventlist\\'	
monthDat=read(path,event_id)
write(monthDat,newpath)
#print(monthDat)	
#n=len(monthDat)
#min_sup=n*0.5
#initSet = tr.createInitSet(monthDat)	
#print(initSet)
#myFPtree, myHeaderTab = tr.createTree(initSet, min_sup)	
#myFPtree.disp()

#freqItemList=tr.findFP(myHeaderTab)	
#print(freqItemList)	
	
#fname='20170801.export.CSV'
#list=day_item(fname, 4)
#print(list)
