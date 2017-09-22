import requests, glob, datetime,re,time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
'''
    This file is used for web crawling,
    the output rows are eventid, date, title, abstract, content
'''

hostlist = ['www.abc.net.au', 'www.news.com.au', 'au.news.yahoo.com','www.smh.com.au','www.dailytelegraph.com.au',
            'www.theage.com.au', 'www.theguardian.com', 'www.brisbanetimes.com.au', 'www.9news.com.au',
            'www.afr.com', 'www.heraldsun.com.au', 'www.couriermail.com.au']


# parse rule for www.abc.net.au
def host1(soup):
    string = ''
    #print(soup.prettify())
    h1Tag = soup.find('h1', itemprop='headline')
    if h1Tag is not None:
        #print('1')
        abstract = stringfy(soup.find('div', class_='tg-tlc-storybody_intro').contents[0])
        string = string + stringfy(h1Tag.contents[0]) + '\t' + abstract + '\t'
        ptags = soup.find('div', class_='tg-tlc-storybody').find_all('p')
        for i in range(0, len(ptags) - 1):
            tag = ptags[i]
            if not tag.has_attr('class'):
                if i == 1:
                    string = string + stringfy(tag.contents[0]).replace('\n', '') + '\t'
                else:
                    if tag.contents[0] != '':
                        string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
        #print(string)
    else:
        #print('2')
        divTag = soup.find("div", class_='article section')
        if divTag is not None:
            h1Tag = divTag.find('h1')
            abstract = ''
            if soup.find('div', class_='tg-tlc-storybody') is not None:
                ptags = soup.find('div', class_='tg-tlc-storybody').find_all('p')
                for i in range(0, len(ptags)):
                    tag = ptags[i]
                    if not tag.has_attr('class'):
                        if tag.contents[0] != '':
                            string = string + stringfy(tag.contents[0]) + ' '
                    elif tag['class'][0] == 'first':
                        abstract = stringfy(tag.contents[0])
                string = stringfy(h1Tag.contents[0]) + '\t' + abstract + '\t' + string
            else:
                #print('3')
                ptags = soup.find('div', class_='article section').find_all('p')
                abstract = stringfy(soup.find('meta', property='og:description')['content'])
                for tag in ptags:
                    if not tag.has_attr('class'):
                        if tag.contents[0] != '':
                            string = string + stringfy(tag.contents[0]) + ' '
                string = stringfy(h1Tag.contents[0]) + '\t' + abstract + '\t' + string
        else:
            #print('4')
            h1Tag = soup.find('h1', itemprop='name')
            if h1Tag is not None:
                title = stringfy(h1Tag.contents[0])
                abstract = title
                comp_texts = soup.find_all('div', class_='comp-rich-text')
                for item in comp_texts:
                    ptags = item.find_all('p')
                    for tag in ptags:
                        if not tag.has_attr('class'):
                            if tag.contents[0] != '':
                                string = string + remove_tag(stringfy(tag.contents[0])) + ' '
                string = title + '\t' + abstract + '\t' + string
            else:
                contentTag = soup.find('div', class_='content')
                if contentTag is not None:
                    title = stringfy(contentTag.find('h1').contents[0])
                    abstract = stringfy(soup.find('meta', attrs={"name": "description"})['content'])
                    ptags = soup.find('div', id='content').find_all('p')
                    for tag in ptags:
                        if not tag.has_attr('class'):
                            if tag.contents[0] != '':
                                string = string + stringfy(tag.contents[0]) + ' '
                        elif tag['class'] == 'first':
                            string = stringfy(tag.contents[0]) + ' ' + string
                    string = title + '\t' + abstract + '\t' + string
                else:
                    contentTag = soup.find('div', id='main')
                    if contentTag is not None:
                        title = stringfy(contentTag.find('h1').contents[0])
                        abstract = title
                        p = soup.find('div', id='article')
                        if p is not None:
                            paragraph = ''
                            for content in p.contents:
                                paragraph = paragraph.strip() + ' ' + remove_tag(
                                    stringfy(content).replace('<br/>', '')).replace(
                                    'Do you have a comment or a story idea? Get in touch with the Lateline team by clicking here.',
                                    '')
                            string = title + '\t' + abstract + '\t' + paragraph
                        else:
                            p = soup.find('div',class_='story')
                            abstract = stringfy(remove_tag(p.find('div',class_='summary').find('p').contents[0]))
                            ptags = p.find('div',class_='story_body').find_all('p')
                            for tag in ptags:
                                if tag.contents[0] != '':
                                    string = string + remove_tag(stringfy(tag.contents[0])) + ' '
                            string = title + '\t' + abstract + '\t' + string
                    else:
                        print('fail')
    return string


# parse www.news.com.au
def host2(soup):
    #print(soup.prettify())
    string = ''
    h1Tag = soup.find('h1', class_='story-headline')
    if h1Tag is not None:
        title = stringfy(h1Tag.contents[0])
        abstract = stringfy(soup.find('p', class_='intro').contents[0])
        string = string + title + '\t' + abstract + '\t'
        ptags = soup.find('div', class_='story-content').find_all('p')
        for tag in ptags:
            if not tag.has_attr('class'):
                paragraph = stringfy(tag.contents[0])
                if not paragraph == '':
                    string = string + stringfy(tag.contents[0]) + ' '
        #print(string)
        return string
    else:
        h1Tag = soup.find('h1', itemprop= 'headline')
        if h1Tag is not None:
            title = stringfy(h1Tag.contents[0])
            abstract = stringfy(soup.find('div', class_='tg-tlc-storybody_intro').contents[0])
            string = string + title + '\t' + abstract + '\t'
            ptags = soup.find('div', class_='tg-tlc-storybody').find_all('p')
            for tag in ptags:
                if not tag.has_attr('class'):
                    paragraph = stringfy(tag.contents[0])
                    if not paragraph == '':
                        string = string + stringfy(tag.contents[0]) + ' '
            #print(string)
            return string


# parse au.news.yahoo.com
def host3(soup):
    string = ''
    title = stringfy(soup.find('h1', class_='headline').contents[0])
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article-container').find_all('p')
    # for tag in ptags:
    for tag in ptags:
        if not tag.has_attr('class'):
            paragraph = stringfy(tag.contents[0])
            if not paragraph == '':
                string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
    return string


# parse www.smh.com.au
def host4(soup):
    string = ''
    title = stringfy(soup.find('header', class_='article__header').find('h1').contents[0])
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__body').find_all('p')
    for tag in ptags:
        if ptags.index(tag) == len(ptags) - 1:
            break
        if not tag.has_attr('class'):
            paragraph = stringfy(tag.contents[0])
            if not paragraph == '':
                string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
    return string


# parse www.dailytelegraph.com.au
def host5(soup):
    string = ''
    title = str(soup.find('h1', itemprop='headline').contents[0]).replace('\n', '').strip()
    abstract = str(soup.find('div', class_='tg-tlc-storybody_intro').contents[0]).replace('\n', '').strip()
    abstract = remove_tag(abstract)
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
    title = str(soup.find('h1').contents[0]).replace('\n', '').strip()
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = str(tag.contents[0])
            if not paragraph == '':
                string = string + str(tag.contents[0]).replace('\n', '') + ' '
    return string


# parse www.theguardian.com
def host7(soup):
    string = ''
    title = stringfy(soup.find('h1', class_='content__headline').contents[0])
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='content__article-body').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = stringfy(tag.contents[0])
            if not paragraph == '':
                string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
    return string


# parse www.brisbanetimes.com.au
def host8(soup):
    string = ''
    title = stringfy(soup.find('h1').contents[0])
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
                        tmp = stringfy(content)
                        content = remove_tag(tmp)
                        paragraph = stringfy(content)
                        if not paragraph == '':
                            string = string + stringfy(paragraph) + ' '
    string = string.replace("By signing up you accept our privacy policy and conditions of use", "").strip()
    return string


# parse www.9news.com.au
def host9(soup):
    string = ''
    title = stringfy(soup.find('h1', class_='article__headline').contents[0])
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__body-croppable').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = stringfy(tag.contents[0])
            if not paragraph == '':
                string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
    string = string.replace("© Nine Digital Pty Ltd 2017", "").strip()
    return string


# parse www.afr.com
def host10(soup):
    string = ''
    title = stringfy(soup.find('h1', itemprop="headline name").contents[0])
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='article__content').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            tmp = stringfy(tag.contents[0])
            content = remove_tag(tmp)
            paragraph = stringfy(content)
            if not paragraph == '':
                string = string + content.replace('\n', '') + ' '
    return string


# parse www.heraldsun.com.au
def host11(soup):
    string = ''
    title = stringfy(soup.find('h1', class_="tg-tlc-storyheader_titlewrapper_h1").contents[0])
    abstract = stringfy(soup.find('div', class_='tg-tlc-storybody_intro').find('p').contents[0])
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find('div', class_='w_tg-tlc-storybody').find_all('p')
    for tag in ptags:
        # if ptags.index(tag) == len(ptags)-1:
        #     break
        if not tag.has_attr('class'):
            paragraph = stringfy(tag.contents[0])
            if not paragraph == '':
                string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
    return string


# parse www.couriermail.com.au
def host12(soup):
    string = ''
    title = stringfy(soup.find('h1').contents[0])
    abstract = title
    string = string + title + '\t' + abstract + '\t'
    ptags = soup.find_all('p')
    for tag in ptags:
        if not tag.has_attr('class'):
            paragraph = ''
            if len(tag.contents) > 0:
                paragraph = stringfy(tag.contents[0])
            if not paragraph == '':
                string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
    return string


def write_to_file(string,path):
    with open(path,'a',encoding='utf-8') as f:
        f.write(string+'\n')


def write_to_log(string):
    with open('dm_crawling.log','a',encoding='utf-8') as f:
        f.write(string+' '+ stringfy(datetime.datetime.now()) +'\n')
def stringfy(c):
    return str(c).replace('\n', '').strip()
def remove_tag(c):
    return re.sub('<[^>]*>', '', c)
# main running part

def main(year):
    filelist = glob.glob('url_201304now/'+stringfy(year)+'/*.CSV')
    for f in filelist:
        filename = f.split('/')[-1]
        write_path = 'news_201304/'+stringfy(year)+'/' + filename
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
                        #print(stringfy(r.url))
                        if r.status_code == 200:
                            string = ''
                            c = r.content
                            soup = BeautifulSoup(c, 'lxml')
                            index = hostlist.index(hostname)
                            if index == 0:
                                # print(url)
                                string = host1(soup)
                                # print(string)
                            elif index == 1:
                                #print(url)
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
                        write_to_log(stringfy(e)+' '+url)
                        print(url)
                        print(e)

