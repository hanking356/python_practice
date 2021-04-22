import pandas as pd
import requests
# bs4 = html parsing
from bs4 import BeautifulSoup
import mysql_movie.webtoon_crud as db

url = "https://comic.naver.com/index.nhn"
result = requests.get(url)
#print(result.content)

# DOM트리로 인식해서 (html문서를 인식해서) return 해서 content에 넣어둠
content = BeautifulSoup(result.content, 'html.parser')

# dt_list는 리스트에서 상속 받음, ResultSet class의 객체, LIST의 상속!
# 인덱싱과 슬라이싱이 된다.
dt_list = content.find_all("div",{"class" : "genreRecomInfo"})
dt_list1 = content.find_all("a",{"class" : "user"})
dt_list2 = content.find_all("div",{"class" : "rating_type"})

tag = dt_list[0].find('a').text
tag1 = dt_list1[0].text
tag2 = dt_list2[0].find('strong').text

#제목 항목을 배열에 저장
title_list = []
for x in range(9):
    data = dt_list[x].find('a').text
    title_list.append(data)
print(title_list)

#id 항목을 배열에 저장
id_list = []
for x in range(9):
    data = dt_list1[x].text
    id_list.append(data)
print(id_list)

#level 항목을 배열에 저장
level_list = []
for x in range(9):
    data = dt_list2[x].find('strong').text
    level_list.append(data)
print(level_list)

#list를 tuple로 변환
title_list2 = tuple(title_list)
id_list2 = tuple(id_list)
level_list2 = tuple(level_list)

#각각의 리스트를 하나로 묶음
total = list(zip(title_list2, id_list2, level_list2))
print(total)
db.create3(total)

# print(tag)
# print(tag1)
# print(tag2)











# print(type(tag))
#
# num_list = content.findAll("span",{"class" : "num"})
# # print(num_list[0].text)
# print('---------------------')
#
# title_list=[]
# for x in dt_list:
#     print(x.find('a').text)
#     data = x.find('a').text
#     title_list.append(data)
# print(len(title_list))
# print(title_list)
#
# jumsu_list = []
# for index in range(0, 145):
#     data = num_list[index].text
#     jumsu_list.append(data)
# print(len(jumsu_list))
# print(jumsu_list)
#
# title_list2 = tuple(title_list)
# #print(title_list2)
# title_list3 = list(title_list2)
# #db.create3(title_list2)
#
# jumsu_list2 = tuple(jumsu_list)
# #print(jumsu_list2)
#
# jumsu_list3 = list(jumsu_list2)
# total = list(zip(title_list2, jumsu_list2))
# print(len(total))
# print(total)
# total2 = tuple(total)
# print(total2)
# db.create3(total)


# for x in range(0, len(num_list), 2):
#     print(num_list[x].text)

# dt_list[0].find('a')
# print(dt_list1.)
