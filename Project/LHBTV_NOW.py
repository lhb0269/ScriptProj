import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkcalendar import Calendar as ca
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

path = "C:/Users/lhb02/Downloads/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
#driver.implicitly_wait(3)

url = "https://www.skysports.com/premier-league-table"
match_day_url = "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2022&month=04&category=epl"
driver.get(url)
page = driver.page_source
pre_team_rank_list = bs(page,"html.parser")
team_rank_list = pre_team_rank_list.find_all ("a" ,{"class" : "standing-table__cell--name-link"})
team_point_list = pre_team_rank_list.find_all("td",{"class" : "standing-table__cell"})

schdule =[]
def make_epl_list(name_list,rank_list,point_list):
    index = 0
    epl_list = []
    for rank in rank_list:
        epl_list.append(rank+".")
    for name in name_list:
        epl_list[index] = epl_list[index] + name
        emptyspace = 50 - len(epl_list[index])
        epl_list[index]+=(" "*(emptyspace-10)+"- 승점 :")
        index += 1
    index = 0
    for point in point_list:
        epl_list[index]=epl_list[index]+point
        index+=1
    return epl_list
def get_epl_data():
    index =0
    team_list = []
    point_list = []
    rank_list = []
    all_data = []
    for team in team_rank_list:
        team_list.append(team.string)

    for text in team_point_list:
        all_data.append(text.string)

    for rank in all_data:
        if index%11 ==0:
            rank_list.append(str(rank))
            index +=1
        else:
            index+=1
    index = 0
    for point in all_data:
        if index == 9:
            point_list.append(str(point))
            index+=1
        elif index==10:
            index = 0
        else :
            index+=1

    epl_list = make_epl_list(team_list, rank_list, point_list)
    return epl_list
def make_schedules():
    trs = pre_match.select('#_monthlyScheduleList > tr')
    no_match = False
    for tr in trs:
        days = tr.select_one('th > div')
        time = tr.select_one('td.time_place > div > span.time')
        if time is None:
            t= '오늘은 경기가 없습니다.'
            no_match = False
        else:
            t=time.text
            no_match = True

        #경기날짜
        if days is not None:
            a= days.text.strip().split(' ')
            day = a[0]
            days_of_weekend = a[1]
        # else:
        #     day = "no_match_day"
        #     days_of_weekend = "no_match"

        #경기장소
        place = tr.select_one('td.time_place > div > span.place')
        if place is not None and no_match is True:
            place = place.text
        else:
            place = "no_match"

        home_team = tr.select_one('div > span.team_left > span.name')
        if home_team is not None and no_match is True:
            home_team = home_team.text
        else:
            home_team = 'no_match'
        away_team = tr.select_one('div > span.team_right > span.name')
        if away_team is not None and no_match is True:
            away_team = away_team.text
        else:
            away_team = 'no_match'

        home_team_score = tr.select_one('div > span.team_left > span.score')
        if home_team_score is not None and no_match is True:
            home_team_score = home_team_score.text
        else:
            home_team_score = '경기 시작전'

        away_team_score = tr.select_one('div > span.team_right > span.score')
        if away_team_score is not None and no_match is True:
            away_team_score = away_team_score.text
        else:
            away_team_score = '경시 시작전'

        # home_team_emblem = tr.select_one('div > span.team_left > img')
        # if home_team_emblem is None and no_match is True:
        #     home_team_emblem = " "
        # else:
        #     home_team_emblem = home_team_emblem['src']
        #     emblem_b = home_team_emblem.split('=')
        #     emblem_c = emblem_b[1].split('&')
        #     home_team_emblem = emblem_c[0]
        #
        # away_team_emblem = tr.select_one('div > span.team_right > img')
        # if away_team_emblem is None and no_match is True:
        #     away_team_emblem = " "
        # else:
        #     away_team_emblem = away_team_emblem['src']
        #     emblem_b = away_team_emblem.split('=')
        #     emblem_c = emblem_b[1].split('&')
        #     away_team_emblem = emblem_c[0]
        #
        # match_detail_link = tr.select_one('td.broadcast > div >a ')
        # if match_detail_link is not None and no_match is True:
        #     match_detail_link = match_detail_link['href']
        # else:
        #     match_detail_link = "경기가 없습니다."

        epl_schedule ={
            'date' :day,
            'day_of_the_week':days_of_weekend,
            'match_times':[t],
            'place':place,
            'home_team':home_team,
            'away_team':away_team,
            'home_team_score':home_team_score,
            'away_team_score':away_team_score,
            #'home_team_emblem':home_team_emblem,
            #'away_team_emblem':away_team_emblem,
            #'match_detail_link':match_detail_link
        }
        schdule.append(epl_schedule)

epl_list = get_epl_data()

driver.get(match_day_url)
page = driver.page_source
pre_match = bs(page,"html.parser")
make_schedules()

for s in schdule:
    c=''
    for value in s.values():
        c+=str(value)+' '
    print(c)
window = Tk()
window.title("LHBTV NOW")
window.geometry("1000x1000+0+0")
window.resizable(False,False)

def stop(event = None):
    window.quit()

text = ScrolledText(width = 50,height = 25)
for team in epl_list:
    text.insert(END,team)
    text.insert(END,'\n')
text.pack(anchor = NW)
cal= ca(window,selectmode='day',year=2022,month=2,day=22)
cal.pack(anchor = NW)

window.bind("<Escape>",stop)
window.mainloop()
