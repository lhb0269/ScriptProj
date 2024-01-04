import re

import exrex
from bs4 import BeautifulSoup
import requests

with open('test.html') as f:
    soup = BeautifulSoup(f,'lxml')

for link in soup.find_all('a'):
    print(link['href'])



headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
keyword = '신라면'
url = f'https://www.google.com/search?q={keyword}'
r = requests.get(url,headers=headers)
if r.ok:
    with open('google_shin_html','wb') as wf:
        wf.write(r.content)
        print(r.text)

soup = BeautifulSoup(r.text,'lxml')
elms = soup.select('div[id = "bres"] a b')
for e in elms:
    print(f'{keyword} {e.string}')

#22-5-18
keyword = '신라면'
url = f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={keyword}&pagingIndex=1&pagingSize=40&productSet=total&query={keyword}&sort=price_asc&timestamp=&viewType=list'
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
r = requests.get(url,headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.text,'lxml')
elms = soup.find_all(class_= re.compile(r'^basicList_title'))

for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^price_num')).string
    print(f'{price}:{title}')