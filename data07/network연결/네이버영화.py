import pandas as pd
import requests
# bs4 = html parsing
from bs4 import BeautifulSoup
import mysql_movie.movie_crud as db

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
#print(result.content)

# DOM트리로 인식해서 (html문서를 인식해서) return 해서 content에 넣어둠
content = BeautifulSoup(result.content, 'html.parser')

# dt_list는 리스트에서 상속 받음, ResultSet class의 객체, LIST의 상속!
# 인덱싱과 슬라이싱이 된다.
dt_list = content.find_all("dt",{"class" : "tit"})

# 리스트의 상속
print(type(dt_list)) #ResultSet클래스의 객체
#print(dt_list) #전체 목록 프린트
print('리스트의 개수>', len(dt_list)) #리스트의 개수
# print(dt_list)
# print(dt_list[0])
tag = dt_list[0].find('a')
print(tag.text)
# print(type(tag))

num_list = content.findAll("span",{"class" : "num"})
# print(num_list[0].text)
print('---------------------')

title_list=[]
for x in dt_list:
    print(x.find('a').text)
    data = x.find('a').text
    title_list.append(data)
print(len(title_list))
print(title_list)

jumsu_list = []
for index in range(0, 145):
    data = num_list[index].text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

title_list2 = tuple(title_list)
#print(title_list2)
title_list3 = list(title_list2)
#db.create3(title_list2)

jumsu_list2 = tuple(jumsu_list)
#print(jumsu_list2)

jumsu_list3 = list(jumsu_list2)
total = list(zip(title_list2, jumsu_list2))
print(len(total))
print(total)
total2 = tuple(total)
print(total2)
db.create3(total)


# for x in range(0, len(num_list), 2):
#     print(num_list[x].text)

# dt_list[0].find('a')
# print(dt_list1.)
