from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

keyword = '신라면'
url = f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={keyword}&pagingIndex=1&pagingSize=40&productSet=total&query={keyword}&sort=price_asc&timestamp=&viewType=list'

browser = webdriver.Chrome()
browser.get(url)
browser.refresh()

html = browser.find_element(By.TAG_NAME,'html')
html.send_keys(Keys.PAGE_DOWN)
#끝까지 스크롤하기
src_count = 0
while src_count < len(browser.page_source):
    src_count = len(browser.page_source)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

from bs4 import BeautifulSoup
import re

keyword = '신라면'
url = f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={keyword}&pagingIndex=1&pagingSize=40&productSet=total&query={keyword}&sort=price_asc&timestamp=&viewType=list'

soup = BeautifulSoup(browser.page_source,'lxml')
elms = soup.find_all(class_= re.compile(r'^basicList_title'))

for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^price_num')).string
    print(f'{price}:{title}')



#과제
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
keyword = '리그 오브 레전드'
url ='https://www.gamemeca.com/ranking.php#ranking-top'
browser = webdriver.Chrome()
browser.get(url)
browser.refresh()


headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(browser.page_source,'lxml')
elms = soup.find_all(class_= re.compile(r'^ranking-table-rows'))
for e in elms:
    name = e.find(class_=re.compile('game-name')).string
    if name == keyword:
        id = e.find(class_=re.compile('gmid'))
        print(id)