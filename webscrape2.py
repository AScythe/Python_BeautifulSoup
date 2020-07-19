import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

res = requests.get(
    'https://www.ptt.cc/bbs/NBA/M.1578380240.A.51D.html', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

images = soup.select('a[href^="https://imgur.com"]')

for image in images:
    print(image['href'])
