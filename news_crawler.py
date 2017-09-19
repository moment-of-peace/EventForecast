import requests, glob, datetime,re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
'''
    This file is used for web crawling,
    the output rows are eventid, date, title, abstract, content
'''

hostlist = ['www.abc.net.au', 'www.news.com.au', 'au.news.yahoo.com','www.smh.com.au','www.dailytelegraph.com.au',
            'www.theage.com.au', 'www.theguardian.com', 'www.brisbanetimes.com.au', 'www.9news.com.au',
            'www.afr.com', 'www.heraldsun.com.au', 'www.couriermail.com.au']

# parse strategy for www.abc.net.au
def host1(soup):
    string = ''
    divTag = soup.find("div", class_='article section')
    title = divTag.find('h1')
    string = string + str(title.contents[0]) + '\t'
    ptags = divTag.find_all('p')
    for i in range(0, len(ptags) - 1):
        tag = ptags[i]
        if not tag.has_attr('class'):
            if i == 1:
                string = string + str(tag.contents[0]).replace('\n', '') + '\t'
            else:
                if tag.contents[0] != '':
                    string = string + str(tag.contents[0]).replace('\n', '') + ' '
    print(string)
    return string

# parse www.news.com.au
def host2(soup):
    string = ''
    title = str(soup.find('h1', class_='story-headline').contents[0])
    abstract = str(soup.find('p', class_='intro').contents[0])
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='story-content').find_all('p')
    for tag in ptags:
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0]).replace('\n', '')
            if not paragraph == '':
                string = string + paragraph + ' '
    return string

# parse au.news.yahoo.com
def host3(soup):
    string = ''
    title = str(soup.find('h1', class_='headline').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article-container').find_all('p')
    # for tag in ptags:
    for tag in ptags:
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    return string

# parse www.smh.com.au
def host4(soup):
    string = ''
    title = str(soup.find('header', class_='article__header').find('h1').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__body').find_all('p')
    for tag in ptags:
        if ptags.index(tag) == len(ptags) - 1:
            break
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    return string

# parse www.dailytelegraph.com.au
def host5(soup):
    string = ''
    title = str(soup.find('h1', itemprop='headline').contents[0]).replace('\n', '').strip()
    abstract = str(soup.find('div', class_='tg-tlc-storybody_intro').find('p').contents[0]).replace('\n', '').strip()
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='tg-tlc-storybody').find_all('p')
    for tag in ptags:
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    string = re.sub('<[^>]*>', '', string).strip()
    return string

# parse www.theage.com.au
def host6(soup):
    string = ''
    title = str(soup.find('h1', itemprop='name headline').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__body').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '

# parse www.theguardian.com
def host7(soup):
    string = ''
    title = str(soup.find('h1', class_='content__headline').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='content__article-body').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    return string

# parse www.brisbanetimes.com.au
def host8(soup):
    string = ''
    title = str(soup.find('h1').contents[0]).replace('\n', '').strip()
    abstract = title
    # print(title)
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('article').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if len(tag.contents) > 1:
            if tag.has_attr('data-reactid'):
                for content in tag.contents:
                    if 'react-text' not in content and content is not None:
                        tmp = str(content)
                        content = re.sub('<[^>]*>', '', tmp)
                        paragraph = str(content).replace('\n', '').strip()
                        if not paragraph == '':
                            string = string + str(paragraph) + ' '
    string = string.replace("By signing up you accept our privacy policy and conditions of use", "").strip()
    return string

# parse www.9news.com.au
def host9(soup):
    string = ''
    title = str(soup.find('h1', class_='article__headline').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__body-croppable').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    string = string.replace("© Nine Digital Pty Ltd 2017", "").strip()
    return string

# parse www.afr.com
def host10(soup):
    string = ''
    title = str(soup.find('h1', itemprop="headline name").contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__content').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            tmp = str(tag.contents[0])
            content = re.sub('<[^>]*>', '', tmp)
            paragraph = str(content)
            if not paragraph == '':
                string = string + content.replace('\n', '') + ' '
    return string

# parse www.heraldsun.com.au
def host11(soup):
    string = ''
    title = str(soup.find('h1', class_="tg-tlc-storyheader_titlewrapper_h1").contents[0]).replace('\n', '').strip()
    abstract = str(soup.find('div', class_='tg-tlc-storybody_intro').find('p').contents[0]).replace('\n', '').strip()
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='w_tg-tlc-storybody').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    return string

# parse www.couriermail.com.au
def host12(soup):
    string = ''
    title = str(soup.find('h1').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find_all('p')
    for tag in ptags:
        if not tag.has_attr('class'):
            paragraph = ''
            if len(tag.contents) > 0:
                paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    return string

def write_to_file(string,path):
    with open(path,'a',encoding='utf-8') as f:
        f.write(string+'\n')
def write_to_log(string):
    with open('dm_crawling.log','a',encoding='utf-8') as f:
        f.write(string+' '+ str(datetime.datetime.now()) +'\n')

# main running part
filelist = glob.glob('url_201304now/2013/*.CSV')
for f in filelist:
    filename = f.split('/')[-1]
    write_path = 'news_201304/2013/' + filename
    with open(f,'r') as file:
        for line in file:
            data = line.split('\t')
            hostname = urlparse(data[5]).hostname
            # if hostname in hostlist:
            if hostname in hostlist:
                url = data[6]
                url = url.replace('\n','')
                eventid = data[0]
                eventdate = data[1]
                try:
                    r = requests.get(url)
                    #print(str(r.url))
                    if r.status_code == 200:
                        string = ''
                        c = r.content
                        soup = BeautifulSoup(c, 'lxml')
                        index = hostlist.index(hostname)
                        if index == 0:
                            string = host1(soup)
                        elif index == 1:
                            string = host2(soup)
                        elif index == 2:
                            string = host3(soup)
                        elif index == 3:
                            string = host4(soup)
                        elif index == 4:
                            string = host5(soup)
                        elif index == 5:
                            string = host6(soup)
                        elif index == 6:
                            string = host7(soup)
                        elif index == 7:
                            string = host8(soup)
                        elif index == 8:
                            string = host9(soup)
                        elif index == 9:
                            string = host10(soup)
                        elif index == 10:
                            string = host11(soup)
                        elif index == 11:
                            string = host12(soup)
                        # finalize the string
                        string = eventid+'\t'+eventdate+'\t'+string
                        write_to_file(string,write_path)
                        write_to_log(eventid)
                except Exception as e:
                    write_to_log(str(e)+' '+url)
                    print(url)
                    print(e)

