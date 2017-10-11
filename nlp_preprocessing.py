import os
import re

# remove stop words, convert to lower case, remove meaningless signals
def clean_news(path, stop_word_list):
    num = 0
    stopWords = set()
    with open(stop_word_list, 'r') as f:
        for line in f:
            stopWords.add(line.strip('\n'))
    flist = os.listdir(path)
    newPath = 'news_clean'
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    # deal with each file
    for f in flist:
        with open(os.path.join(path,f), 'r') as src:
            string = '' # will be written into target file
            line = src.readline().strip('\n')
            while line != '':
                newLine = ''
                content = line.split('\t')
                # ignore no id events
                if len(content) < 3:
                    line = src.readline().strip('\n')
                    continue

                if content[2] != '':    # ignore empty news
                    # replace tab with space
                    for i in range(3, len(content)):
                        content[2] = content[2] + ' ' + content[i]
                    # to lower case, then split and remove meaningless signals
                    words = re.split('[^a-zA-Z0-9$]', content[2].lower())
                    for word in words:
                        if (word not in stopWords) and word != '':
                            newLine = newLine + word + ' '
                    string = string + '%s\t%s\n'%(content[0], newLine)
                    num += 1
                line = src.readline().strip('\n')
        with open(os.path.join(newPath,f), 'w') as tar:
            tar.write(string)
    print('total news: %d'%(num))

# count the length distribution of news
def counter(path):
    dic = dict()
    flist = os.listdir(path)
    for f in flist:
        with open(os.path.join(path,f),'r') as fid:
            for line in fid:
                num = len(line.split(' '))
                num = int(num/1500)
                if num in dic.keys():
                    dic[num] += 1
                else:
                    dic[num] = 1
    return dic

# get the corresponding attributes (number of mentions, sentiments, etc) of each news
def matchId(srcPath, tarPath):
    flist = os.listdir(tarPath)
    newPath = 'news_match'
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    for f in flist:
        idDic = dict()
        src, tar = os.path.join(srcPath,f), os.path.join(tarPath,f)
        f1 = open(src,'r')
        f2 = open(tar,'r')
        line = f1.readline().strip('\n')
        while line != '':
            content = line.split('\t')
            idDic[content[0]] = (content[25],content[29],content[30],content[31],content[32],content[33],content[34])
            line = f1.readline().strip('\n')
        line = f2.readline().strip('\n')
        string = ''
        while line != '':
            index = line.find('\t')
            attr = idDic[line[:index]]
            string += merge(attr, line[index+1:])
            line = f2.readline().strip('\n')
        out = open(os.path.join(newPath,f),'w')
        out.write(string)
        f1.close(), f2.close(), out.close()
def merge(attr, line):
    s = ''
    for e in attr:
        s = s + e + '\t'
    s = s + line + '\n'
    return s

# average the attributes of duplicated news
def attr_ave(path):
    newPath = 'news_ave'
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    flist = os.listdir(path)
    for f in flist:
        attrs = dict()
        news, newsSet = list(), set()
        string = ''
        with open(os.path.join(path,f),'r') as src:
            for line in src:
                upgradeAttr(news, attrs, line)
        for e in news:
            key = e[30:60]
            if key not in newsSet:
                string = string + attr_to_str(attrs[key]) + e + '\n'
                newsSet.add(key)
        # write the average results
        with open(os.path.join(newPath,f),'w') as tar:
            tar.write(string)

# upgrade the attributes of a news when reading a new line
def upgradeAttr(news, attrs, line):
    content = line.strip('\n').split('\t')
    news.append(content[7])
    key = content[7][30:60]
    item = [1]
    item.extend(content[0:7])
    for i in range(len(item)):
        try:    # none
            item[i] = float(item[i])
        except:
            item[i] = 0
    if key in attrs.keys():
        for i in range(len(item)):
            attrs[key][i] += item[i]
    else:
        attrs[key] = item

# convert a series attributes to a string
def attr_to_str(attr):
    l = list()
    num = int(attr[0])
    # compute average
    for i in range(1, len(attr)):
        l.append(float(attr[i])/num)
    # convert to string
    string = ''
    for e in l:
        string = string + str(round(e,2)) + '\t'
    return string

# join all file and generate a single file
def join_files(path):
    flist = os.listdir(path)
    num = 0
    string = ''
    with open(newFile, 'w') as tar:
        for f in flist:
            with open(os.path.join(path,f),'r') as src:
                line = src.readline().strip('\n')
                while line != '':
                    num += 1
                    string = string + line + '\n'
                    if num%500 == 0:
                        print(num)
                        tar.write(string)
                        string = ''
                    line = src.readline().strip('\n')
        if string != '':
            tar.write(string)
                    
#clean_news('news_201304', 'stop_words2.txt')
#matchId('201304now','news_clean')
#attr_ave('news_match')
