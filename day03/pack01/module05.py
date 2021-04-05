#문자열 포맷팅

p = '이름: %s, 나이:%d' %('홍길동', 100)
print(p)

p2 = 'X = %0.3f, Y= %10.2f' % (3.1456, 555.666)
print(p2)

##############################################
#문자열 추출: indexing(인덱싱) ==> slicing(슬라이싱)
name = '홍길동'
print(name[0])
print(name[1])
print(name[0:2]) #0부터 끝까지
print(name[1:]) #1부터 끝까지
print(name[:2]) #1부터 시작짜지
print(type(name[0]))

hobby = '달리기,등산,자전거,코딩'
#split을 해주면 list로 만들어줌
result = hobby.split(',')
print(result)
print(type(result))
print(result[0])
print(result[3])

s = "이름:{0}, 나이:{1}"
sf = s.format("이대준", 300)
print(sf)

s2 = "이름:{name}, 나이:{age}"
sf2 = s.format(name = "이대준",age =  300)
print(sf2)

data = (10, 20, 30)
s3 = "길이:{data[0]}, 높이:{data[1]}, 면적:{data[2]},"
sf2 = s3.format(d = data)
print(sf3)