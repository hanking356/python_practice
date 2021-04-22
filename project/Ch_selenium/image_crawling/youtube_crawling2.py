import pandas as pd # 데이터를 처리하기 위한 가장 기본적인 패키지
from selenium import webdriver # 웹 브라우저의 동작을 제어하기 위한 프로토콜
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver import Chrome
import re
from selenium.webdriver.chrome.options import Options
import datetime as dt
import pyperclip
import openpyxl #엑셀을 제어할 수 있는 라이브러리

# 1. Workbook 생성
wb = openpyxl.Workbook()
# 2. Sheet 활성
sheet = wb.active
# 3. 데이터프레임 내 header(변수명)생성
sheet.append(["VNUM", "VDATE1", "VVIDEO", "IMAGE", "TITLE", "CLICKS", "GOOD", "BADD","CHANNEL"])

url = 'https://www.youtube.com'
driver = webdriver.Chrome('../ driver/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

# 웹 페이지 가져오기
driver.get(url)

driver.find_elements_by_xpath('//*[@id="search"]')[0].click() #검색창영역클릭
driver.find_elements_by_xpath('//*[@id="search"]')[0].send_keys('FM247 HD')#검색창 영역에 원하는 youtuber입력
driver.find_elements_by_xpath('//*[@id="search"]')[0].send_keys(Keys.RETURN)#엔터

driver.find_elements_by_xpath('//*[@id="avatar-section"]/a')[0].click() #개인 유튜브 홈페이지
driver.find_elements_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')[0].click() #동영상 클릭

body = driver.find_element_by_tag_name('body')#스크롤하기 위해 소스 추출

num_pagedowns = 3
#10번 밑으로 내리는 것
while num_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    num_pagedowns -= 1

html0 = driver.page_source
html = BeautifulSoup(html0,'html.parser')

video_list0 = html.find_all('ytd-grid-video-renderer',{'class':'style-scope ytd-grid-renderer'})
print(len(video_list0))

url = 'https://www.youtube.com/'
#len(video_list0)
for i in range(30):
    per_url = url + video_list0[i].find('a',{'id':'thumbnail'})['href'] #개인 유튜브 url
    name = video_list0[i].find('a', {'id': 'video-title'}).text #동영상 제목
    thumm = video_list0[i].find('img', {'id': 'img'}).get('src') #동영상 썸네일
    meta = video_list0[i].find('div', {'id': 'metadata-line'}) #동영상 조회수 div
    view = meta.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0].text.split()[1] #동영상 조회수
    view2 = view[:-1]
    # 조회수 문자를 숫자로 변환하는 작업
    if view2[-1] == '천':
        view2 = float(view2[:-1])*1000
    elif view2[-1] == '만':
        view2 = float(view2[:-1]) * 10000
    elif view2[-1] == '억':
        view2 = float(view2[:-1]) * 100000000

    #개인 유튜브 페이지 접속
    driver.get(per_url)
    time.sleep(3)
    html2 = driver.page_source
    html3 = BeautifulSoup(html2,'html.parser')

    #개인 동영상 url
    driver.find_elements_by_xpath("//*[@id='top-level-buttons']/ytd-button-renderer[1]/a")[0].click()
    driver.find_elements_by_xpath("//*[@id='target']/yt-icon")[0].click()
    copy = driver.find_elements_by_xpath("//*[@id='textarea']")[0]
    copy.click()
    copy.send_keys(Keys.CONTROL + 'c')
    per_video = pyperclip.paste()
    per_video2 = per_video.split()
    per_video3 = per_video2[3][5:-1]

    thumm = video_list0[i].find('img', {'id': 'img'}).get('src')
    # 동영상 게시 날짜
    date = html3.find('div', {'id': 'date'}).text[1:12]
    date2 = date.replace(". ","-")

    # 좋아요수
    likes_num = html3.find('yt-formatted-string', {'id': 'text', 'class':
        'style-scope ytd-toggle-button-renderer style-text'}).text + '개'
    likes_num2 = likes_num[:-1]
    if likes_num2[-1] == '천':
        likes_num2 = float(likes_num2[:-1])*1000
    elif likes_num2[-1] == '만':
        likes_num2 = float(likes_num2[:-1]) * 10000
    elif likes_num2[-1] == '억':
        likes_num2 = float(likes_num2[:-1]) * 100000000

    # 싫어요수
    unlikes_num = html3.find('yt-formatted-string', {'id': 'text', 'class': 'style-scope ytd-toggle-button-renderer style-text',
                                                     'aria-label': re.compile('싫어요')}).text + '개'
    unlikes_num2 = unlikes_num[:-1]
    if unlikes_num2[-1] == '천':
        unlikes_num2 = float(unlikes_num2[:-1]) * 1000
    elif unlikes_num2[-1] == '만':
        unlikes_num2 = float(unlikes_num2[:-1]) * 10000
    elif unlikes_num2[-1] == '억':
        unlikes_num2 = float(unlikes_num2[:-1]) * 100000000

    # sheet.append(["VNUM", "VDATE1", "VVIDEO", "IMAGE", "TITLE", "CLICKS", "GOOD", "BADD", "CHANNEL"])
    print(i, per_video3, name, thumm, view2, likes_num2, unlikes_num2, date2)
    # sheet 내 각 행에 데이터 추가
    sheet.append([i, date2, per_video3, thumm, name,  view2, likes_num2, unlikes_num2, 'FM247 HD'])

    wb.save("youtube_tv.xlsx")



