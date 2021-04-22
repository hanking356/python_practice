import mysql_bbs.bbs_dao as db

no= input('순서를 입력하세요')
title = input('제목을 입력하세요')
content = input('내용을 입력하세요')
writer = input('작가를 입력하세요')

data = (no, title, content, writer)
print('입력된 데이터들', data)
db.create(data)