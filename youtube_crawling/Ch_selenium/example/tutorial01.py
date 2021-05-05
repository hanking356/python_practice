#tutorial01.py
#selenium이 설치되었는지 확인!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
# 크롬드라이버를 만들 변수 설정

url = "https://www.google.co.kr"

driver = webdriver.Chrome('../ driver/chromedriver.exe')
driver.implicitly_wait(3)#묵시적 대기


# 페이지 가져온다(이동)
driver.get(url)

time.sleep(5)
driver.quit()

