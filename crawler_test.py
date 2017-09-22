import glob,requests,re
from bs4 import BeautifulSoup
hostlist = ['www.abc.net.au', 'www.news.com.au', 'au.news.yahoo.com','www.smh.com.au','www.dailytelegraph.com.au',
            'www.theage.com.au', 'www.theguardian.com', 'www.brisbanetimes.com.au', 'www.9news.com.au',
            'www.afr.com', 'www.heraldsun.com.au', 'www.couriermail.com.au']

url = 'http://www.theage.com.au/victoria/metropolitan-fire-brigade-staff-win-big-pay-rises-20140101-3063h.html'
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, 'lxml')
def stringfy(c):
    return str(c).replace('\n', '').strip()
def remove_tag(c):
    return re.sub('<[^>]*>', '', c)
'''
www.abc.net.au

'''
# string = ''
# print(soup.prettify())
# h1Tag = soup.find('h1',itemprop='headline')
# if h1Tag is not None:
#     print('1')
#     abstract = stringfy(soup.find('div',class_='tg-tlc-storybody_intro').contents[0])
#     string = string + stringfy(h1Tag.contents[0])+'\t'+ abstract + '\t'
#     ptags = soup.find('div',class_='tg-tlc-storybody').find_all('p')
#     for i in range(0, len(ptags) - 1):
#         tag = ptags[i]
#         if not tag.has_attr('class'):
#             if i == 1:
#                 string = string + stringfy(tag.contents[0]).replace('\n', '') + '\t'
#             else:
#                 if tag.contents[0] != '':
#                     string = string + stringfy(tag.contents[0]).replace('\n', '') + ' '
#     print(string)
# else:
#     print('2')
#     divTag = soup.find("div", class_='article section')
#     if divTag is not None:
#         h1Tag = divTag.find('h1')
#         abstract = ''
#         if soup.find('div', class_='tg-tlc-storybody') is not None:
#             ptags = soup.find('div', class_='tg-tlc-storybody').find_all('p')
#             for i in range(0, len(ptags)):
#                 tag = ptags[i]
#                 if not tag.has_attr('class'):
#                     if tag.contents[0] != '':
#                             string = string + stringfy(tag.contents[0]) + ' '
#                 elif tag['class'][0] == 'first':
#                     abstract = stringfy(tag.contents[0])
#             string = stringfy(h1Tag.contents[0]) + '\t' + abstract + '\t' + string
#         else:
#             print('3')
#             ptags = soup.find('div', class_='article section').find_all('p')
#             abstract = stringfy(soup.find('meta',property='og:description')['content'])
#             for tag in ptags:
#                 if not tag.has_attr('class'):
#                     if tag.contents[0] != '':
#                         string = string + stringfy(tag.contents[0]) + ' '
#             string = stringfy(h1Tag.contents[0]) + '\t' + abstract + '\t' + string
#     else:
#         print('4')
#         h1Tag = soup.find('h1',itemprop='name')
#         if h1Tag is not None:
#             title = stringfy(h1Tag.contents[0])
#             abstract = title
#             comp_texts = soup.find_all('div', class_='comp-rich-text')
#             for item in comp_texts:
#                 ptags = item.find_all('p')
#                 for tag in ptags:
#                     if not tag.has_attr('class'):
#                         if tag.contents[0] != '':
#                             string = string + remove_tag(stringfy(tag.contents[0])) + ' '
#             string = title + '\t' + abstract + '\t' + string
#         else:
#             contentTag = soup.find('div', class_='content')
#             if contentTag is not None:
#                 title = stringfy(contentTag.find('h1').contents[0])
#                 abstract = stringfy(soup.find('meta',attrs={"name":"description"})['content'])
#                 ptags = soup.find('div', id='content').find_all('p')
#                 for tag in ptags:
#                     if not tag.has_attr('class'):
#                         if tag.contents[0] != '':
#                             string = string + stringfy(tag.contents[0]) + ' '
#                     elif tag['class'] == 'first':
#                         string = stringfy(tag.contents[0])+ ' ' + string
#                 string = title + '\t' + abstract + '\t' + string
#             else:
#                 contentTag = soup.find('div', id='main')
#                 if contentTag is not None:
#                     title = stringfy(contentTag.find('h1').contents[0])
#                     abstract = title
#                     p = soup.find('div', id='article')
#                     if p is not None:
#                         paragraph = ''
#                         for content in p.contents:
#                             paragraph = paragraph.strip() + ' ' + remove_tag(
#                                 stringfy(content).replace('<br/>', '')).replace(
#                                 'Do you have a comment or a story idea? Get in touch with the Lateline team by clicking here.',
#                                 '')
#                         string = title + '\t' + abstract + '\t' + paragraph
#                     else:
#                         p = soup.find('div', class_='story')
#                         abstract = stringfy(remove_tag(p.find('div', class_='summary').find('p').contents[0]))
#                         ptags = p.find('div', class_='story_body').find_all('p')
#                         for tag in ptags:
#                             if tag.contents[0] != '':
#                                 string = string + remove_tag(stringfy(tag.contents[0])) + ' '
#                         string = title + '\t' + abstract + '\t' + string
#                 else:
#                     print('fail')
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
# string = ''
# title = str(soup.find('h1', class_='story-headline').contents[0])
# abstract = str(soup.find('p', class_='intro').contents[0])
# string = string + title + '\t' + abstract + '\t'
# ptags = soup.find('div',class_='story-content').find_all('p')
# for tag in ptags:
#     if not tag.has_attr('class'):
#         paragraph = str(tag.contents[0])
#         if not paragraph == '':
#             string = string + str(tag.contents[0]) + ' '
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
# string = ''
# title = str(soup.find('h1', itemprop='headline').contents[0]).replace('\n', '').strip()
# abstract = str(soup.find('div', class_='tg-tlc-storybody_intro').contents[0]).replace('\n', '').strip()
# abstract = remove_tag(abstract)
# string = string + title + '\t' + abstract + '\t'
# ptags = soup.find('div',class_='tg-tlc-storybody').find_all('p')
# for tag in ptags:
#     if not tag.has_attr('class'):
#         paragraph = str(tag.contents[0])
#         if not paragraph == '':
#             string = string + str(tag.contents[0]).replace('\n', '') + ' '
# string = re.sub('<[^>]*>', '', string).strip()
print(string)