# tutorial02.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('../ driver/chromedriver.exe')
driver.implicitly_wait(3)

# #화면크기
# driver.fullscreen_window()#전체모드
# time.sleep(1)
# driver.maximize_window()#최대창
driver.set_window_rect(-10,0,500,500)

# 크기정보
print(driver.get_window_rect())


time.sleep(3)
driver.quit()