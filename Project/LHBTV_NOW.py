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
driver.implicitly_wait(3)

url = "https://www.skysports.com/premier-league-table"
driver.get(url)
page = driver.page_source
pre_team_rank_list = bs(page,"html.parser")
team_rank_list = pre_team_rank_list.find_all ("a" ,{"class" : "standing-table__cell--name-link"})
team_point_list = pre_team_rank_list.find_all("td",{"class" : "standing-table__cell"})

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

epl_list = get_epl_data()
window = Tk()
window.title("LHBTV NOW")
window.geometry("1000x1000+0+0")
window.resizable(False,False)

def stop(event = None):
    window.quit()

text = ScrolledText(width = 50,height = 50)
for team in epl_list:
    text.insert(END,team)
    text.insert(END,'\n')
text.pack()
cal= ca(window,selectmode='day',year=2022,month=2,day=22)
cal.pack()

window.bind("<Escape>",stop)
window.mainloop()
