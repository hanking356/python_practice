# tutorial03.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('../ driver/chromedriver.exe')
driver.implicitly_wait(3)

##페이지 가져오기
driver.get('https://google.co.kr')
driver.get('https://naver.com')
driver.get('https://youtube.com/c/반원')

#이전 창 이동
driver.back()
time.sleep(.5)
driver.back()
time.sleep(.5)

#앞으로 이동
driver.forward()
time.sleep(.5)
driver.forward()
time.sleep(.5)


time.sleep(3)
driver.quit()