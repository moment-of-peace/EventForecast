import os
import treeNode as tr
from orangecontrib.associate.fpgrowth import *


def day_item(fname, event_id):
    reader = open(path + fname, 'r', encoding='utf-8')
    # writer=open(newfname,'w',endcoding='utf-8')

    dic = {}
    for line in reader:
        print(line)
        columns = line.strip('\n').split('\t')

        if columns[event_id] in dic.keys():
            dic[columns[event_id]] = dic[columns[event_id]] + 1
        else:
            dic[columns[event_id]] = 1
            # print(dic)
            # if len(list)>10:#source data so long, cause memory error
            # break

    return dic


def day_list(dic, min):
    list = []
    x = dic.keys()
    for key in x:
        if dic[key] > min:
            list.append(key)
    return list


def read(path, event_id):
    monthDat = []
    flist = os.listdir(path)
    for f in flist:
        dic = day_item(f, event_id)
        list = day_list(dic, 1000)
        monthDat.append(list)
    return monthDat


"""def clean_fl(freqItemList):
    freqItemSet=[]
    for item in freqItemList:
        if len(item)>1:
            freqItemSet.append(item)
    return freqItemSet"""


def write(freqItemList, newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    writer = open(newpath + 'input_data.csv', 'w')
    for l in freqItemList:
        for item in l:
            writer.write(item + ',')
        writer.write('\n')
    writer.close()


path = 'del_201304now/'
event_id = 4
monthDat = read(path, event_id)
new_item_set = []
for i in range(0,len(monthDat), 5):
    tmp_array = []
    if i+4>len(monthDat)-1:
        for k in range(i,len(monthDat)):
            tt = monthDat[k]
            for t1 in tt:
                if not t1 in tmp_array:
                    tmp_array.append(t1)
    else:
        for j in range(0,5):
            tt = monthDat[j]
            for t1 in tt:
                if not t1 in tmp_array:
                    tmp_array.append(t1)
    new_item_set.append(tmp_array)
itemsets = dict(frequent_itemsets(new_item_set, .75))
rules = association_rules(itemsets, .75)
rules = list(rules)
with open('ex_output.txt','a') as of:
    for rule in rules:
        of.write(str(rule)+'\n')

# n = len(monthDat)
# min_sup = n * 0.5
# initSet = tr.createInitSet(monthDat)
# print(initSet)
# myFPtree, myHeaderTab = tr.createTree(initSet, min_sup)
# # myFPtree.disp()
#
# freqItemList = tr.findFP(myHeaderTab)
#
# # print(freqItemList)
# # freqItemSet=clean_fl(freqItemList)
# """
# freqItemSet=[]
# for item in freqItemList:
#     if len(item)>1:
#         freqItemSet.append(item)
# print(freqItemSet)"""
# newpath = 'freqItemList/'
# write(freqItemList, newpath)
# dic=day_item('20170802.export.CSV',4)
# print(dic)
# x=dic.keys()
# print(x)
# list=day_list(dic,500)
# print(list)
