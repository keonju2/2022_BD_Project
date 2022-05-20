import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import exceptions


pd.set_option('display.max_columns', None)
s = Service(ChromeDriverManager().install())


def crawler(company,date_1,date_2,max_page):
    total_results = pd.DataFrame(columns={'Company','Title','Date','Source','Link'})

    for page in range(int(max_page)):
        driver = webdriver.Chrome(service=s)
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=0&photo=0&field=0&pd=3&ds={1}&de={2}&cluster_rank=10&mynews=1&office_type=1&office_section_code=3&news_office_checked=1009&&start={3}1'.format(company,date_1,date_2,page)
        driver.get(url)
        html = driver.page_source
        bs0bj = BeautifulSoup(html, 'lxml')
        time.sleep(3)

        title_list = []
        date_list = []
        source_list = []
        link_list = []
        company_list = []
        news_info = bs0bj.find_all('div','news_area')

        for i in range(len(news_info)):

            news_title = news_info[i].find('a',class_ ='news_tit').text
            title_list.append(news_title)

            news_link = news_info[i].find('a',class_ = 'news_tit')['href']
            link_list.append(news_link)

            date_info = news_info[i].select('span.info')
            for j in date_info:
                date = j.text
                if re.search(r'\d+.\d+.\d+.',date) != None:
                    date_list.append(date)


            source = '매일경제'
            source_list.append(source)
            company_list.append(company)
        total = {'Company':company_list,'Title':title_list,'Date':date_list,'Source':source_list,'Link':link_list}
        total = pd.DataFrame(total)
        total_results = total_results.append(total,ignore_index=True)




        driver.quit()

    return total_results



finals = pd.DataFrame()

final = crawler('네이버','2021.01.01','2021.06.30','276')
finals = pd.concat([finals,final],ignore_index=True)

final = crawler('네이버','2021.07.01','2021.12.31','197')
finals = pd.concat([finals,final],ignore_index=True)

finals.to_csv('네이버_1년.csv',index=False,encoding='utf-8')


finals = pd.DataFrame()
final = crawler('카카오','2021.01.01','2021.06.30','234')
pd.concat([finals,final],ignore_index=True)

final = crawler('카카오','2021.07.01','2021.12.31','250')
pd.concat([finals,final],ignore_index=True)

finals.to_csv('카카오_1년.csv',index=False,encoding='utf-8')
