import db연결.mysql연결모듈 as db

id = input('아이디를 입력하세요')
pw = input('패스워드를 입력하세요')
name = input('이름을 입력하세요')
tel = input('전화번호를 입력하세요')

data = (id, pw, name, tel)
print('입력된 데이터들', data)
db.create2(data)