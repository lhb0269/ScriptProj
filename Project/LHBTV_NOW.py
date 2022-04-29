import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkcalendar import Calendar as ca
import re
import datetime

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

path = "C:/Users/lhb02/Downloads/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)

d=datetime.date.today()
month =f"{d.month}"
day = f"{d.month}.{d.day}"
url = "https://www.skysports.com/premier-league-table"
driver.get(url)
page = driver.page_source
pre_team_rank_list = bs(page,"html.parser")
team_rank_list = pre_team_rank_list.find_all ("a" ,{"class" : "standing-table__cell--name-link"})
team_point_list = pre_team_rank_list.find_all("td",{"class" : "standing-table__cell"})

schdule =[]
champs=[]
list=[]
team_list=[]
favorite_team=''
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
            place = None

        home_team = tr.select_one('div > span.team_left > span.name')
        if home_team is not None and no_match is True:
            home_team = home_team.text
        else:
            home_team = ' '
        away_team = tr.select_one('div > span.team_right > span.name')
        if away_team is not None and no_match is True:
            away_team = away_team.text
        else:
            away_team = ' '

        home_team_score = tr.select_one('div > span.team_left > span.score')
        if home_team_score is not None and no_match is True:
            home_team_score = home_team_score.text
        else:
            home_team_score = ' '

        away_team_score = tr.select_one('div > span.team_right > span.score')
        if away_team_score is not None and no_match is True:
            away_team_score = away_team_score.text
        else:
            away_team_score = ' '
        epl_schedule ={
            'date' :day,
            'day_of_the_week':days_of_weekend,
            'match_times':t,
            'place':place,
            'home_team':home_team,
            'away_team':away_team,
            'home_team_score':home_team_score,
            'away_team_score':away_team_score,
            #'home_team_emblem':home_team_emblem,
            #'away_team_emblem':away_team_emblem,
            #'match_detail_link':match_detail_link
        }
        list.append(home_team)
        schdule.append(epl_schedule)
def make_schedules_champs():
    global list
    trs = pre_match.select('#_monthlyScheduleList > tr')
    no_match = False
    for tr in trs:
        days = tr.select_one('th > div')
        time = tr.select_one('td.time_place > div > span.time')
        if time is None:
            t = '오늘은 경기가 없습니다.'
            no_match = False
        else:
            t = time.text
            no_match = True

        # 경기날짜
        if days is not None:
            a = days.text.strip().split(' ')
            day = a[0]
            days_of_weekend = a[1]
        place = tr.select_one('td.time_place > div > span.place')
        if place is not None and no_match is True:
            place = place.text
        else:
            place = None

        home_team = tr.select_one('div > span.team_left > span.name')
        if home_team is not None and no_match is True:
            home_team = home_team.text
        else:
            home_team = ' '
        away_team = tr.select_one('div > span.team_right > span.name')
        if away_team is not None and no_match is True:
            away_team = away_team.text
        else:
            away_team = ' '

        home_team_score = tr.select_one('div > span.team_left > span.score')
        if home_team_score is not None and no_match is True:
            home_team_score = home_team_score.text
        else:
            home_team_score = ' '

        away_team_score = tr.select_one('div > span.team_right > span.score')
        if away_team_score is not None and no_match is True:
            away_team_score = away_team_score.text
        else:
            away_team_score = ' '
        champs_schedule = {
            'date': day,
            'day_of_the_week': days_of_weekend,
            'match_times': t,
            'place': place,
            'home_team': home_team,
            'away_team': away_team,
            'home_team_score': home_team_score,
            'away_team_score': away_team_score,
        }
        champs.append(champs_schedule)

epl_list = get_epl_data()

match_day_url = f"https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2022&month={month}&category=epl"
driver.get(match_day_url)
page = driver.page_source
pre_match = bs(page,"html.parser")
make_schedules()

chaps_day_url = "https://sports.news.naver.com/wfootball/schedule/index?category=champs"
driver.get(chaps_day_url)
page = driver.page_source
pre_match = bs(page,"html.parser")
make_schedules_champs()

#좋아하는 팀 리스트
for v in list:
    if v not in team_list and v != ' ':
        team_list.append(v)

window = Tk()
window.title("LHBTV NOW")
window.geometry("1280x1000+0+0")
window.resizable(False,False)

def stop(event = None):
    window.quit()
def select_day(code):#날짜 선택
    target = re.compile(day)
    if code == 1:
        input_text = schdule_text.get("1.0",END)
        lines = input_text.splitlines()
        schdule_text.tag_remove('found', "1.0", END)
    elif code == 2:
        input_text = champs_schdule_text.get("1.0",END)
        lines = input_text.splitlines()
        champs_schdule_text.tag_remove('found', "1.0", END)

    for i,line in enumerate(lines):
        for mo in target.finditer(line):
            if code == 1:
                schdule_text.tag_add('found',f"{i+1}.0+{mo.span()[0]}chars",f"{i+1}.0+{mo.span()[1]}chars")
            if code == 2:
                champs_schdule_text.tag_add('found',f"{i+1}.0+{mo.span()[0]}chars",f"{i+1}.0+{mo.span()[1]}chars")
#좋아하는 팀 선택
def select_team(event=None):
    global favorite_team
    for i in favorite_team_listbox.curselection():
        favorite_team=favorite_team_listbox.get(i)
    target = re.compile(favorite_team)
    input_text = schdule_text.get("1.0",END)
    lines = input_text.splitlines()

    schdule_text.tag_remove('found',"1.0",END)
    for i,line in enumerate(lines):
        for mo in target.finditer(line):
            schdule_text.tag_add('found', f"{i + 1}.0+{mo.span()[0]}chars", f"{i + 1}.0+{mo.span()[1]}chars")
    alam(favorite_team)
def alam(team):
    now = time.localtime()
    match_time=""
    for s in schdule:
        if str(s.get('date')) == day:
            if str(s.get('home_team')) == team or str(s.get('away_team')) == team:
                match_time = str(s.get('match_times')).replace(":","")
    if match_time == "":
        return False
    now = int(f"{now.tm_hour}{now.tm_min}")
    match_time = int(match_time)
    if match_time - now < 30:
       messagebox.showinfo(title="알림",message="경기 시작 30분 전")

def get_day(event = None):#달력에서 날짜 정보 가져오기
    global day
    date = (cal.get_date())
    new_day=date.replace('/','.')
    new_day=new_day.split('.')
    day=f"{new_day[0]}.{new_day[1]}"
    schdule_text.bind(select_day(1))
    champs_schdule_text.bind(select_day(2))
text = ScrolledText(width = 50,height = 25)
for team in epl_list:
    text.insert(END,team)
    text.insert(END,'\n')
text.place(x = 0,y = 0)
cal= ca(window,selectmode='day',year=2022,month=4,day=23)
cal.place(x=0,y=330)


team_listbox = Listbox(selectmode = 'single',height = 15)


schdule_text = ScrolledText(width = 100,height = 30)
schdule_text.tag_configure('found',background = 'blue',foreground = 'purple')
for s in schdule:
    if s.get('place') is not None:
        c = str(s.get('date'))+' '+str(s.get('day_of_the_week'))+' '+str(s.get('match_times'))+' '+s.get('place')+' '+\
            s.get('home_team')+' vs '+s.get('away_team')+' '+str(s.get('home_team_score'))+ ' : '+str(s.get('away_team_score'))
        schdule_text.insert(END,c)
        schdule_text.insert(END,'\n')
schdule_text.pack(anchor = E)
schdule_text.bind(select_day(1))


champs_schdule_text = ScrolledText(width = 100,height = 30)
champs_schdule_text.tag_configure('found',background = 'blue',foreground = 'purple')
for s in champs:
    if s.get('place') is not None:
        c = str(s.get('date'))+' '+str(s.get('day_of_the_week'))+' '+str(s.get('match_times'))+' '+s.get('place')+' '+\
            s.get('home_team')+' vs '+s.get('away_team')+' '+str(s.get('home_team_score'))+ ' : '+str(s.get('away_team_score'))
        champs_schdule_text.insert(END,c)
        champs_schdule_text.insert(END,'\n')
champs_schdule_text.pack(anchor = E)
champs_schdule_text.bind(select_day(2))

favorite_team_listbox = Listbox(selectmode = 'single',height = 10)
for v in team_list:
    favorite_team_listbox.insert(END,v)
favorite_team_listbox.place(x=0,y=500)
favorite_team_listbox.bind('<<ListboxSelect>>',select_team)

window.bind("<Escape>",get_day)
window.mainloop()
