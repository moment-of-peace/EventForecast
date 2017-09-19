import glob,requests,re
from bs4 import BeautifulSoup
hostlist = ['www.abc.net.au', 'www.news.com.au', 'au.news.yahoo.com','www.smh.com.au','www.dailytelegraph.com.au',
            'www.theage.com.au', 'www.theguardian.com', 'www.brisbanetimes.com.au', 'www.9news.com.au',
            'www.afr.com', 'www.heraldsun.com.au', 'www.couriermail.com.au']

url = 'http://www.theage.com.au/comment/privacy-rights-reform-must-prevail-over-naked-ambition-20140907-10divz.html'
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, 'lxml')
'''
www.news.com.au

string = ''
title = str(soup.find('h1', class_='story-headline').contents[0])
abstract = str(soup.find('p', class_='intro').contents[0])
string = string + title + '\t' + abstract + '\t'
ptags = soup.find('div',class_='story-content').find_all('p')
for tag in ptags:
    if not tag.has_attr('class'):
        paragraph = str(tag.contents[0])
        if not para
        string = string + str(tag.contents[0]) + ' '
'''

'''
au.news.yahoo.com

string = ''
title = str(soup.find('h1', class_='headline').contents[0]).replace('\n','').strip()
abstract = title
string = string + title + '\t' + abstract + '\t'
ptags = soup.find('div', class_='article-container').find_all('p')
# for tag in ptags:
for tag in ptags:
    if not tag.has_attr('class'):
        paragraph = str(tag.contents[0])
        if not paragraph == '':
            string = string + str(tag.contents[0]) + ' '
print(string)
'''
'''
www.smh.com.au

string = ''
title = str(soup.find('header', class_='article__header').find('h1').contents[0]).replace('\n', '').strip()
abstract = title
string = string + title + '\t' + abstract + '\t'
ptags = soup.find('div', class_='article__body').find_all('p')
for tag in ptags:
    if ptags.index(tag) == len(ptags)-1:
        break
    if not tag.has_attr('class'):
        paragraph = str(tag.contents[0])
        if not paragraph == '':
            string = string + str(tag.contents[0]).replace('\n', '') + ' '
'''

#todo unsolve js generated files from www.dailymail.co.uk
'''
www.dailymail.co.uk

string = ''
print(soup.prettify())
title = str(soup.find('div', class_='article-text wide').find('h1').contents[0]).replace('\n', '').strip()
abstract = ''
lis = soup.find('ul',class_='mol-bullets-with-font').find_all('li')
for li in lis:
    abstract = abstract + str(li.contents[0]).replace('\n', '').strip()
string = string + title + '\t' + abstract + '\t'
ptags = soup.find('div', itemprop='articleBody').find_all('p',class_='mol-para-with-font')
for tag in ptags:
    if ptags.index(tag) == len(ptags) - 1:
        break
    if not tag.has_attr('class'):
        paragraph = str(tag.contents[0])
        if not paragraph == '':
            print(paragraph)
            string = string + str(tag.contents[0]).replace('\n', '') + ' '
'''

'''
www.theage.com.au

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
'''

'''
www.theage.com.au

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
'''
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
'''
www.brisbanetimes.com.au

string = ''
title = str(soup.find('h1').contents[0]).replace('\n', '').strip()
abstract = title
# print(title)
string = string + title + '\t' + abstract + '\t'
ptags = soup.find('article').find_all('p')
for tag in ptags:
    # if ptags.index(tag) == len(ptags)-1:
    #     break
    if len(tag.contents)>1:
        if tag.has_attr('data-reactid'):
            for content in tag.contents:
                if 'react-text' not in content and content is not None:
                    tmp = str(content)
                    content = re.sub('<[^>]*>', '', tmp)
                    paragraph = str(content).replace('\n', '').strip()
                    if not paragraph == '':
                        string = string + str(paragraph) + ' '
string = string.replace("By signing up you accept our privacy policy and conditions of use", "").strip()
print(string)
'''
'''
http://www.9news.com.au

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
string = string.replace("© Nine Digital Pty Ltd 2017","").strip()
'''

'''
http://www.afr.com

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
print(string)
'''


'''
http://www.heraldsun.com.au

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
'''

'''
http://www.couriermail.com.au/

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
'''

'''
www.dailytelegraph.com.au
string = ''
title = str(soup.find('h1', itemprop='headline').contents[0]).replace('\n', '').strip()
abstract = str(soup.find('div', class_='tg-tlc-storybody_intro').find('p').contents[0]).replace('\n', '').strip()
string = string + title + '\t' + abstract + '\t'
ptags = soup.find('div',class_='tg-tlc-storybody').find_all('p')
for tag in ptags:
    if not tag.has_attr('class'):
        paragraph = str(tag.contents[0])
        if not paragraph == '':
            string = string + str(tag.contents[0]).replace('\n', '') + ' '
string = re.sub('<[^>]*>', '', string).strip()
'''

print(string)