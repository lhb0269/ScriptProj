import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

path = "C:/Users/lhb02/Downloads/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
driver.implicitly_wait(3)

url = "https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&tab=team"
driver.get(url)
page = driver.page_source
pre_team_rank_list = bs(page,"html.parser")
team_rank_list = pre_team_rank_list.select("#wfootballTeamRecordBody>table>tbody>tr")

score_list=[]
for team in team_rank_list:
    num = team.select('.num > div.inner > strong')[0].text
    name = team.select('.name')[0].text
    score = team.select(".selected > div.inner")[0].text
    print(score)