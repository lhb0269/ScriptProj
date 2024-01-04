import time

import pyautogui

pyautogui.PAUSE = 1#delay
pyautogui.FAILSAFE = True #탈출,네군데 모서리 마우스 이동시 에러 발생

w,h = pyautogui.size()
print(w,h)

# for i in range(10):
#     pyautogui.moveTo(100,100,duration= 0.25)
#     pyautogui.moveTo(200,100,duration= 0.25)
#     pyautogui.moveTo(200,200,duration= 0.25)
#     pyautogui.moveTo(100,200,duration= 0.25)

# pyautogui.doubleClick(480,296)
# pyautogui.scroll(-500)
# import time
# time.sleep(3)
# pyautogui.scroll(500)

#im = pyautogui.screenshot('screen.png') #im 은 PIL image

# p = pyautogui.locateCenterOnScreen('1.png')
#
# for i in range(10):
#     pyautogui.click(p[0],p[1])

time.sleep(2)
pyautogui.click(1365,340)
pyautogui.screenshot('weatherreport.png')