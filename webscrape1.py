# web scrapping practice
import requests
# request is a package to link with the web
from bs4 import BeautifulSoup
# first pip install bs4 first then beautiful soup
# beautifulsoup get info from the website

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
# headers used to pretend you are not crawling and just visiting
# headers -- request header -- user-agent


res = requests.get("https://www.economist.com/latest/", headers=headers)
# get/post can be seen in developer tools -- network -- choose any -- headers
# post - if you have something to do first before entering the website
# in case you put headers, then you have to put 'headers=headers' on request
soup = BeautifulSoup(res.text, "html.parser")
# x.text if you like to get text
# instead of 'html5lib', you can use 'html.parser' or 'lxml' - different method for different information
news = soup.find('div', 'teaser-list').find_all('article', 'teaser')
# select an element using the arrow
# use to find info that you like
# 'div' is a tag, 'teaser-list' is a class
# 'article' is a tag, 'teaser' is a class

# def get_url():
#   url = []
#   for time, article in enumerate(news):
#     # enumerate has 2 values index and element
#     # time is the index of the news, article is element in list

#     # print('\n### Find number {} "img" section in news ###\n'.format(time))
#     # print(article.find('img'))

#     print('\nget number {} "src" class in img section'.format(time) )
#     print('URL: {}'.format(article.find('img').get('src')))
#     url.append(article.find('img').get('src'))
#     # get takes the "=" (equivalent) of the class scr
#   print(url)

all_title = []
for new in news:
    all = dict()
    all[' GROUP '] = new.find('a', 'teaser__link').find(
        'div', 'teaser__group-text').find('h3').find('', 'flytitle-and-title__flytitle').text
    all[' TITLE '] = new.find('a', 'teaser__link').find('div', 'teaser__group-text').find(
        'h3', 'flytitle-and-title__body').find('span', 'flytitle-and-title__title').text
    all[' DESRIPTION '] = new.find('a', 'teaser__link').find(
        'div', 'teaser__group-text').find('div', 'teaser__text').text
    all[' PICTURE '] = new.find('img').get('src')
    all_title.append(all)
    # know the difference between get and text later

for all in all_title:
    print(all)

# get_url()
