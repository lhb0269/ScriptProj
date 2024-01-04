from selenium import webdriver
import time
import pyautogui
import pyperclip

options = webdriver.ChromeOptions()
user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
options.add_experimental_option('excludeSwitches',['enable-automation'])
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options)
target_url = 'https://www.naver.com'
browser.get(target_url)
time.sleep(2)
#날씨 들어가기
pyautogui.click(1379,303)
time.sleep(2)
pyautogui.screenshot('weatherreport.png')

#화면상의 카카오톡 클릭 및 단톡방 들어가기
pyautogui.click(625,1068)
pyautogui.doubleClick(206,123)

#내 화면상의 디렉토리 접근 및 이미지 옮기기 작업 디렉토리가 열려있다는 가정하에
pyautogui.click(518,1056)
pyautogui.click(286,653)

#드래그
pyautogui.click(1068,394)
time.sleep(1)
pyautogui.dragTo(1579,900,duration= 1)
pyautogui.click(1474,770)
pyautogui.press('enter')