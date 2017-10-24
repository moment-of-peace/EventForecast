import os
import treeNode as tr
def day_item(fname,event_id):
	day_event=[]
	reader=open(path+fname,'r',encoding='utf-8')
	#writer=open(newfname,'w',endcoding='utf-8')
	list=[]
	for line in reader:
		columns=line.strip('\n').split('\t')
		if len(list)>10:#source data so long, cause memory error
			break
		if columns[event_id] not in list:
			list.append(columns[event_id])
			
	return list	

def read(path,event_id):
	monthDat=[]
	flist=os.listdir(path)
	for f in flist:
		list=day_item(f,event_id)
		monthDat.append(list)
	return monthDat	

event_id=4
path='C:\\Users\\12444\\Documents\\study\\master2\\dataMining\\project\\data_mining_five_day\\'		
monthDat=read(path,event_id)
#print(monthDat)	
n=len(monthDat)
min_sup=4
initSet = tr.createInitSet(monthDat)	
#print(initSet)
myFPtree, myHeaderTab = tr.createTree(initSet, min_sup)	
myFPtree.disp()

freqItemList=tr.findFP(myHeaderTab)	
print(freqItemList)	
	
#fname='20170801.export.CSV'
#list=day_item(fname, 4)
#print(list)
