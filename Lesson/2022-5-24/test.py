from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import requests

#봇 키
key = '5587375417:AAG9AB8nf59EUNU3nz9a5JWq1LNnR4OI2_8'
r = requests.get(f'https://api.telegram.org/bot{key}/getMe')

r.headers
r.headers['content-type']
r.json()

sender_id = None
def print_msg(msg):
    global sender_id
    sender_id = msg['from']['id']
    sender = msg['from']['first_name']
    text = msg['text']
    print(f'{sender}({sender_id}): {text}')
    if text =='!help':
        send_msg()
def send_msg():
    global r
    url = f'https://api.telegram.org/bot{key}/sendMessage'
    params = {
        'chat_id' : sender_id,
        'text' : '안녕하세욤'
    }
    r = requests.get(url,params=params)
url = f'https://api.telegram.org/bot{key}/getUpdates'
r=requests.get(url)
r.json()
alist=[]
if len(r.json()['result']):
    update_list = r.json()['result']
    for update in update_list:
        alist.append(update)
        print_msg(update['message'])
    last_update_id = alist[-1]['update_id']
    params ={
        'offset': last_update_id + 1
    }
    r= requests.get(url,params=params)
    r.json()
    if r.ok:
        update_list = r.json()['result']
        for update in update_list:
            print_msg(update['message'])





# url입력
driver = webdriver.Chrome('C:/ScriptProj/2022-5-24/chromedriver.exe') # 크롬드라이버 경로 설정
url = "https://www.yogiyo.co.kr/" # 사이트 입력
driver.get(url) # 사이트 오픈
driver.maximize_window() # 전체장
time.sleep(2) # 2초 지연

# 검색창 선택
xpath = '''//*[@id="search"]/div/form/input'''  # 검색창
element = driver.find_element_by_xpath(xpath)
element.clear()
time.sleep(2)

# 검색창 입력
value = input("지역을 입력하세요")
element.send_keys(value)
time.sleep(2)

# 조회버튼 클릭
search_xpath = '''//*[@id="button_search_address"]/button[2]'''
driver.find_element_by_xpath(search_xpath).click()

time.sleep(3)

# 검색 콤보상자 선택
# 선택 : #search > div > form > ul > li:nth-child(3) > a
search_selector = '#search > div > form > ul > li:nth-child(3) > a'
search = driver.find_element_by_css_selector(search_selector)
search.click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 스크롤을 가장 아래로 내린다
time.sleep(2)
pre_height = driver.execute_script("return document.body.scrollHeight") # 현재 스크롤 위치 저장

while True :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
    cur_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤을 저장한다.
    if pre_height == cur_height :
        break
    pre_height == cur_height


time.sleep(3)

# 페이지 소스 출력
html = driver.page_source
html_source = BeautifulSoup(html, 'html.parser')


# 데이터 추출
restaurant_name = html_source.find_all("div", class_ = "restaurant-name ng-binding") #업체명
restaurant_score = html_source.find_all("span", class_ = "ico-star1 ng-binding") #별점
restaurant_review = html_source.find_all("span", attrs = {"class":"review_num ng-binding", "ng-show":"restaurant.review_count > 0"}) # 리뷰 수
restaurant_ceo_review = html_source.find_all("span", attrs = {"class":"review_num ng-binding", "ng-show":"restaurant.owner_reply_count > 0"}) # 사장님 리뷰
del_limit = html_source.find_all("li", class_ = "delivery-time ng-binding") # 배달소요시간

sub_list = []
result_list = []
#데이터 배열
for i, j, k, l, m in zip(restaurant_name, restaurant_score, restaurant_review, restaurant_ceo_review, del_limit) :
    sub_list.append(i.string) # 업체명
    sub_list.append(j.string.replace("★ ","")) # 별점 스코어
    sub_list.append(re.sub(" |\n|리뷰","",k.string)) # 리뷰 수
    sub_list.append(re.sub(" |\n|사장님댓글","",l.string)) # 사장님 리뷰
    sub_list.append(m.string.replace("\n","").replace(" ","")) # 배달소요시간
    result_list.append(sub_list) # 리스트 요소 추가
    sub_list = [] # 변수 초기화

time.sleep(30)
driver.close() # 크롬드라이버 종료