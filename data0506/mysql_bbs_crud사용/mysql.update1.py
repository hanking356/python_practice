import mysql_bbs.bbs_dao as db

no = input('순서를 입력하세요')
title = input('제목을 입력하세요')

db.update(no, title)