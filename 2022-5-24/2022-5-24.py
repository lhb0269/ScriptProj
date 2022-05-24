from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests


keyword = '신라면'
#url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}"
url = 'https://flyasiana.com/I/KR/KO/RevenueRegistTravel.do'
options = webdriver.ChromeOptions()
user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'

options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option('excludeSwitches',['enable-automation'])
browser = webdriver.Chrome(options=options)

browser.get(url)
#browser.refresh()

#편도에 대한 xPath
xpath = '//*[@id="container"]/div[2]/div[1]/ul/li[2]/a'
browser.find_element(By.XPATH,xpath).click()
time.sleep(1)

xpath = '//*[@id="txtDepartureAirport1"]'
browser.find_element(By.XPATH,xpath).click()
browser.find_element(By.XPATH,xpath).send_keys('GMP')
browser.find_element(By.XPATH,xpath).send_keys(Keys.ENTER)
time.sleep(1)

xpath='//*[@id="txtArrivalAirport1"]'
browser.find_element(By.XPATH,xpath).click()
browser.find_element(By.XPATH,xpath).send_keys('CJU')
browser.find_element(By.XPATH,xpath).send_keys(Keys.ENTER)
time.sleep(1)

xpath = '//*[@id="divCalendarContainer"]/label'
browser.find_element(By.XPATH,xpath).click()
time.sleep(1)

xpath = "//*[@class='calendar_top']/select/option[text()= ' 2022.06']"
browser.find_element(By.XPATH,xpath).click()

xpath = '//td[@data-handler="selectDay"]/a[text()="25"]'
browser.find_element(By.XPATH,xpath).click()

xpath = '//*[@id="btn_searchFlight"]'
browser.find_element(By.XPATH,xpath).click()

xpath = '//*[@id="btnAuCase2"]'
browser.find_element(By.XPATH,xpath).click()


# soup = BeautifulSoup(browser.page_source,features='lxml')
# elms = soup.find_all(class_ = '_image _listImage')


# for i,e in enumerate(elms[:10]):
#     caption = e['alt']
#     image_url = e['data-lazy-src'] if e.has_attr('data-lazy-src') else e['src']
#     print(f'No:{i},Caption: {caption} ,Source:{image_url}')
#     r = requests.get(image_url)
#     r.raise_for_status()
#     if r.headers['Content-Type'].endswith('jpeg'):
#         with open(f'downloaded_{i:02}.jpg','wb') as f:
#             f.write(r.content)