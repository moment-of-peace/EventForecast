
#variables:
#name of the node, a count
#nodelink used to link similar items
#parent vaiable used to refer to the parent of the node in the tree
#node contains an empty dictionary for the children in the node
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      #needs to be updated
        self.children = {} 
#increments the count variable with a given amount    
    def inc(self, numOccur):
        self.count += numOccur
#display tree in text. Useful for debugging        
    def disp(self, ind=1):
        print ('  '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)


def createTree(dataSet, minSup=1): #create FP-tree from dataset but don't mine
    headerTable = {}
    #go over dataSet twice
    for trans in dataSet:#first pass counts frequency of occurance
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in list(headerTable):  #remove items not meeting minSup
        if headerTable[k] < minSup: 
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    #print 'freqItemSet: ',freqItemSet
    if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 
    #print 'headerTable: ',headerTable
    retTree = treeNode('Null Set', 1, None) #create tree
    for tranSet, count in dataSet.items():  #go through dataset 2nd time
        localD = {}
        for item in tranSet:  #put transaction items in order
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)#populate tree with ordered freq itemset
    return retTree, headerTable #return tree and header table

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:#check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count) #incrament count
    else:   #add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: #update header table 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):   #this version does not use recursion
    while (nodeToTest.nodeLink != None):    #Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

def ascendTree(leafNode, prefixPath): #ascends from leaf node to root
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(treeNode): #treeNode comes from header table
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def condTree(basePat,headerTable, minSup):
    dic={}
    for a in headerTable.items():
        x=a[1][0]
        dic[a[0]]=x

    
    
	
def mineTree(basePat, headerTable, minSup, preFix, freqItemList):
    dic={}
    for a in headerTable.items():
        x=a[1][0]
        dic[a[0]]=x
    
    bigL = [v[0] for v in sorted(dic.items(), key=lambda p: p[1])]
    # (sort header table)
    for basePat in bigL: # start from bottom of header table
        newFreqSet = preFix.copy()
        newFreqSet.append(basePat)
        # print ‘finalFrequent Item: ‘,newFreqSet #append to set
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(headerTable[basePat][1])
        # print ‘condPattBases :’,basePat, condPattBases
        # 2. construct cond FP-tree from cond. pattern base
        myCondTree, myHead = createTree(condPattBases, minSup)
        #print(freqItemList)
        # print ‘head from conditional tree: ‘, myHead
        if myHead != None: # 3. mine cond. FP-tree
            # print ‘conditional tree for: ‘,newFreqSet
            # myCondTree.disp(1)
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)
 
def findFP(myHeaderTab):
    preFix=[]
    freqItemList=[]
    mineTree('',myHeaderTab,3,preFix,freqItemList)
    #for item in freqItemList:
        #if len(item)<2:
            #freqItemList.remove(item)
    return freqItemList
    

"""rootNode = treeNode('pyramid',9,None)
rootNode.children['eye'] = treeNode('eye',13,None)
rootNode.disp()
simpDat = loadSimpDat()
simpDat
initSet = createInitSet(simpDat)
initSet

#The FP-tree
myFPtree, myHeaderTab = createTree(initSet, 3)
myFPtree.disp()
findPrefixPath(myHeaderTab['x'][1])
findPrefixPath(myHeaderTab['r'][1])
#mineTree('',myHeaderTab,3,preFix=[],freqItemList=[])
freqItemList=findFP()
freqItemList
"""

#variables:
#name of the node, a count
#nodelink used to link similar items
#parent vaiable used to refer to the parent of the node in the tree
#node contains an empty dictionary for the children in the node
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      #needs to be updated
        self.children = {} 
#increments the count variable with a given amount    
    def inc(self, numOccur):
        self.count += numOccur
#display tree in text. Useful for debugging        
    def disp(self, ind=1):
        print ('  '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)


def createTree(dataSet, minSup=1): #create FP-tree from dataset but don't mine
    headerTable = {}
    #go over dataSet twice
    for trans in dataSet:#first pass counts frequency of occurance
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in list(headerTable):  #remove items not meeting minSup
        if headerTable[k] < minSup: 
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    #print 'freqItemSet: ',freqItemSet
    if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 
    #print 'headerTable: ',headerTable
    retTree = treeNode('Null Set', 1, None) #create tree
    for tranSet, count in dataSet.items():  #go through dataset 2nd time
        localD = {}
        for item in tranSet:  #put transaction items in order
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)#populate tree with ordered freq itemset
    return retTree, headerTable #return tree and header table

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:#check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count) #incrament count
    else:   #add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: #update header table 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):   #this version does not use recursion
    while (nodeToTest.nodeLink != None):    #Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

def ascendTree(leafNode, prefixPath): #ascends from leaf node to root
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(treeNode): #treeNode comes from header table
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def condTree(basePat,headerTable, minSup):
    dic={}
    for a in headerTable.items():
        x=a[1][0]
        dic[a[0]]=x

    
    
	
def mineTree(basePat, headerTable, minSup, preFix, freqItemList):
    dic={}
    for a in headerTable.items():
        x=a[1][0]
        dic[a[0]]=x
    
    bigL = [v[0] for v in sorted(dic.items(), key=lambda p: p[1])]
    # (sort header table)
    for basePat in bigL: # start from bottom of header table
        newFreqSet = preFix.copy()
        newFreqSet.append(basePat)
        # print ‘finalFrequent Item: ‘,newFreqSet #append to set
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(headerTable[basePat][1])
        # print ‘condPattBases :’,basePat, condPattBases
        # 2. construct cond FP-tree from cond. pattern base
        myCondTree, myHead = createTree(condPattBases, minSup)
        #print(freqItemList)
        # print ‘head from conditional tree: ‘, myHead
        if myHead != None: # 3. mine cond. FP-tree
            # print ‘conditional tree for: ‘,newFreqSet
            # myCondTree.disp(1)
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)
 
def findFP(myHeaderTab):
    preFix=[]
    freqItemList=[]
    mineTree('',myHeaderTab,3,preFix,freqItemList)
    """for item in freqItemList:
        if len(item)<2:
            freqItemList.remove(item)"""
    return freqItemList



"""rootNode = treeNode('pyramid',9,None)
rootNode.children['eye'] = treeNode('eye',13,None)
rootNode.disp()
simpDat = loadSimpDat()
simpDat
initSet = createInitSet(simpDat)
initSet

#The FP-tree
myFPtree, myHeaderTab = createTree(initSet, 3)
myFPtree.disp()
findPrefixPath(myHeaderTab['x'][1])
findPrefixPath(myHeaderTab['r'][1])
#mineTree('',myHeaderTab,3,preFix=[],freqItemList=[])
freqItemList=findFP()
freqItemList
"""
