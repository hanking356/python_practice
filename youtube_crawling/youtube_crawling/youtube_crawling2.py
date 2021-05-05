from selenium import webdriver # 웹 브라우저의 동작을 제어하기 위한 프로토콜
from selenium.webdriver.common.keys import Keys #키 입력과 클릭을 위한 모듈
import time #시간 데이터 처리
from bs4 import BeautifulSoup #html문서 parsing 라이브러리
from selenium.webdriver import Chrome #구글 브라우저 원격 제어 webdriver
import re #정규 표현식
import pyperclip #복사/붙여넣기 클립보드
import openpyxl #엑셀 제어 라이브러리

# 1. Workbook 생성
wb = openpyxl.Workbook()
# 2. Sheet 활성
sheet = wb.active
# 3. 데이터프레임 내 header(변수명)생성
sheet.append(["VNUM", "VDATE1", "VVIDEO", "IMAGE", "TITLE", "CLICKS", "GOOD", "BADD","CHANNEL"])

url = 'https://www.youtube.com' #유뷰트 주소
driver = webdriver.Chrome('../ driver/chromedriver.exe') #구글브라우저 호출
driver.implicitly_wait(5) #웹 페이지 로딩 대기
driver.maximize_window() #브라우저 화면 최대화

driver.get(url) # 유튜브 페이지 가져오기

# xpath를 이용하여 html태그와 속성 탐색
driver.find_elements_by_xpath('//*[@id="search"]')[0].click() #검색창영역클릭
driver.find_elements_by_xpath('//*[@id="search"]')[0].send_keys('FM247 HD') #검색창 영역에 채널입력
driver.find_elements_by_xpath('//*[@id="search"]')[0].send_keys(Keys.RETURN) #엔터키 입력
driver.find_elements_by_xpath('//*[@id="avatar-section"]/a')[0].click() #채널 유튜브 홈페이지
driver.find_elements_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')[0].click() #동영상 버튼 클릭


num_pagedowns = 10 #page 내리는 횟수 설정

while num_pagedowns:
    body.send_keys(Keys.PAGE_DOWN) # html 페이지 내리기
    time.sleep(1) #시간(초) 간격
    num_pagedowns -= 1

body = driver.find_element_by_tag_name('body')#body 태그 요소 소스 추출
html1 = driver.page_source #현재 렌더링 된 페이지의 Elements를 추출
html2 = BeautifulSoup(html1,'html.parser') #Elements 저장

video_list0 = html.find_all('ytd-grid-video-renderer',{'class':'style-scope ytd-grid-renderer'})

#video_list0 길이만큼 시행
for i in range(len(video_list0)):
    per_url = url + video_list0[i].find('a',{'id':'thumbnail'})['href'] #개인 유튜브 url
    name = video_list0[i].find('a', {'id': 'video-title'}).text #동영상 제목
    image = video_list0[i].find('img', {'id': 'img'}).get('src') #동영상 썸네일
    meta = video_list0[i].find('div', {'id': 'metadata-line'}) #동영상 조회수 div
    view = meta.find_all('span', {'class': 'style-scope ytd-grid-video-renderer'})[0].text.split()[1] #동영상 조회수
    view2 = view[:-1]

    #개인 동영상 소스 코드 추출
    driver.find_elements_by_xpath("//*[@id='top-level-buttons']/ytd-button-renderer[1]/a")[0].click()
    driver.find_elements_by_xpath("//*[@id='target']/yt-icon")[0].click()
    copy = driver.find_elements_by_xpath("//*[@id='textarea']")[0]
    copy.click()
    copy.send_keys(Keys.CONTROL + 'c')
    per_video = pyperclip.paste()
    per_video2 = per_video.split()
    per_video3 = per_video2[3][5:-1]

    # 개인 유튜브 페이지 접속
    driver.get(per_url)
    time.sleep(3)
    html3 = driver.page_source
    html4 = BeautifulSoup(html3, 'html.parser')

    # 동영상 게시 날짜
    date = html3.find('div', {'id': 'date'}).text[1:12]
    date2 = date.replace(". ","-")

    # 좋아요수
    likes_num = html3.find('yt-formatted-string', {'id': 'text', 'class':
        'style-scope ytd-toggle-button-renderer style-text'}).text

    # 싫어요수
    unlikes_num = html3.find('yt-formatted-string',
                             {'id': 'text', 'class': 'style-scope ytd-toggle-button-renderer style-text',
                              'aria-label': re.compile('싫어요')}).text

    # 문자열 -> 숫자형으로 변환
    # 1. 조회수
    if view2[-1] == '천':
        view2 = float(view2[:-1]) * 1000
    elif view2[-1] == '만':
        view2 = float(view2[:-1]) * 10000
    elif view2[-1] == '억':
        view2 = float(view2[:-1]) * 100000000

    # 2.좋아요 수
    likes_num2 = likes_num[:-1]
    if likes_num2[-1] == '천':
        likes_num2 = float(likes_num2[:-1])*1000
    elif likes_num2[-1] == '만':
        likes_num2 = float(likes_num2[:-1]) * 10000
    elif likes_num2[-1] == '억':
        likes_num2 = float(likes_num2[:-1]) * 100000000

    # 3. 싫어요 수
    unlikes_num2 = unlikes_num[:-1]
    if unlikes_num2[-1] == '천':
        unlikes_num2 = float(unlikes_num2[:-1]) * 1000
    elif unlikes_num2[-1] == '만':
        unlikes_num2 = float(unlikes_num2[:-1]) * 10000
    elif unlikes_num2[-1] == '억':
        unlikes_num2 = float(unlikes_num2[:-1]) * 100000000

    print(i, per_video3, name, image, view2, likes_num2, unlikes_num2, date2)

    # sheet 내 각 행에 데이터 추가
    sheet.append([i, date2, per_video3, image, name,  view2, likes_num2, unlikes_num2, 'FM247 HD'])

    # exel파일에 저장
    wb.save("youtube_tv.xlsx")



