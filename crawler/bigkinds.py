import time
import pyautogui
import pyperclip
import cv2


def imgClick(filename, t):
    imgfile = pyautogui.locateOnScreen(filename,confidence = 0.8)
    center = pyautogui.center(imgfile)
    pyautogui.moveTo(center)
    pyautogui.click(center)
    time.sleep(t)


def scroll(line):
    time.sleep(0.5)
    pyautogui.scroll(line)
    time.sleep(0.5)


keywords = ['((네이버) OR (네이버(주)) OR (NAVER))','((카카오) OR ((주)카카오) OR (kakao))']
time.sleep(1)
kakao_list = [('2017-07-01','2017-12-31'),('2018-01-01','2018-06-30'),('2018-07-01','2018-12-31'),('2019-01-01','2019-06-30'),('2019-07-01','2019-12-31'),('2020-01-01','2020-06-30'),('2021-07-01','2021-12-31'),('2021-01-01','2021-06-30'),('2021-07-01','2021-12-31')]
naver_list =[('2014-01-01','2014-06-30'),('2014-07-01','2014-12-31'),('2015-01-01','2015-06-30'),('2015-07-01','2015-12-31'),('2016-01-01','2016-06-30'),('2016-07-01','2016-12-31'),('2017-01-01','2017-06-30'),('2017-07-01','2017-12-31'),('2018-01-01','2018-06-30'),('2018-07-01','2018-12-31'),('2019-01-01','2019-06-30'),('2019-07-01','2019-12-31'),('2020-01-01','2020-06-30'),('2021-07-01','2021-12-31'),('2021-01-01','2021-06-30'),('2021-07-01','2021-12-31')]

imgClick('search.png',0.2)
pyautogui.hotkey('ctrl','a')
pyautogui.press('delete')
pyperclip.copy(keywords[1])
pyautogui.hotkey('ctrl','v')
imgClick('time.png', 0.2)
'''
    if i == 0:
        for search_time in naver_list:
            imgClick('time1.png',0.2)
            pyautogui.doubleClick()
            pyperclip.copy(search_time[0])
            pyautogui.hotkey('ctrl', 'v')

            imgClick('time2.png', 0.2)
            pyautogui.doubleClick()
            pyperclip.copy(search_time[1])
            pyautogui.hotkey('ctrl', 'v')

            scroll(-300)
            imgClick('accept.png', 5)

            while True:
                try:
                    imgClick('step3.png', 3)
                    break
                except:
                    scroll(-300)

            while True:
                try:
                    imgClick('excel.png',3)
                    break
                except:
                    scroll(-300)
'''
for search_time in kakao_list:
    imgClick('time1.png',0.2)
    pyautogui.doubleClick()
    pyperclip.copy(search_time[0])
    pyautogui.hotkey('ctrl', 'v')

    imgClick('time2.png', 0.2)
    pyautogui.doubleClick()
    pyperclip.copy(search_time[1])
    pyautogui.hotkey('ctrl', 'v')

    scroll(-300)
    imgClick('accept.png', 5)

    while True:
        try:
            imgClick('step3.png', 5)
            break
        except:
            scroll(-300)

    while True:
        try:
            imgClick('excel.png',5)
            break
        except:
            scroll(-300)

    while True:
        try:
            imgClick('return.png',10)
            break
        except:
            scroll(300)








