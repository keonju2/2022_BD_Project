import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import re
import time

pd.set_option('display.max_columns', None)

s = Service('chromedriver.exe')

def crawler(company_name,company_code,start_page,end_page):

    total_result = pd.DataFrame(columns = {'Company','Title','Link','Date','Chat'})
    for page in range(int(start_page), int(end_page)+1):
        driver = webdriver.Chrome(service=s)
        url = 'https://finance.naver.com/item/board.naver?code=' + str(company_code) + '&page=' + str(page)
        driver.get(url)
        html = driver.page_source
        bs0bj = BeautifulSoup(html, 'lxml')
        time.sleep(3)

        titles = bs0bj.find_all('td','title')
        title_result = []
        link_result = []
        date_result = []
        for title in titles:
            chat_title = title.get_text()
            chat_title = re.sub('\n', '', chat_title)
            chat_title = re.sub('\t', '', chat_title)
            title_result.append(chat_title)
            add = 'https://finance.naver.com' + title.find('a')['href']
            link_result.append(add)


        dates = bs0bj.find_all('span','tah p10 gray03')

        for date in dates:
            chat_date = date.get_text()
            if re.search(r'\d+.\d+.\d+.',chat_date) != None:
                date_result.append(chat_date)

        company_result = [company_name for date in date_result]


        for i in range(len(link_result)):
            total = {'Company':company_result[i],'Title':title_result[i],'Link':link_result[i],'Date':date_result[i]}
            driver.get(link_result[i])
            html = driver.page_source
            bs0bj = BeautifulSoup(html, 'lxml')
            time.sleep(3)

            main_chat = bs0bj.find('div', id='body')
            main_chat = main_chat.text
            main_chat = re.sub('\n', '', main_chat)
            main_chat = re.sub('\t', '', main_chat)
            total['Chat'] = main_chat
            total_result = total_result.append(total, ignore_index=True)
        driver.quit()

    return total_result

result = crawler('카카오','035720','1817','7739')
result.to_csv('카카오_토론방.csv',index=False,encoding='utf-8')