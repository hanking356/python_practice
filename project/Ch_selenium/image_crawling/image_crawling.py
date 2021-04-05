#image_crawling
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

keyword = input("수집할 이미지: ")
url = "https://search.naver.com/search.naver?where=image&query={}".format(keyword)
driver = webdriver.Chrome('../ driver/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

# 웹 페이지 가져오기
driver.get(url)

# 이미지 요소(elements) 수집하기
imgs = driver.find_elements_by_css_selector('img._image')
#print(len(imgs))
links = []
for img in imgs:
    link = img.get_attribute('src')
    if 'http' in link:
        links.append(link)
#pprint(links)

##다운로드-파일이름(확장자 ex)jpg, png), 파일저장위치
# ~~~.jpg&~~~
# ->.jpg만 추출하기 위해 find 또는 rfind함수와 슬라이싱을 이용
for index, link in enumerate(links):
    start = link.rfind('.')
    end = link.rfind('&')
    filetype = link[start:end]
    print(filetype)
    filename = "{0}{1:03d}{2}".format(keyword,index,filetype)
    urlretrieve(link, filename)





time.sleep(3)
driver.quit()
