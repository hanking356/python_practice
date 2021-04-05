#기본형 4가지
#정수, 실수

age = 100 #정수(int)
weight = 99.9 #실수(float)

sum2 = age + weight #더하기 연산자
#하나라도 스트링이 들어가 있으면 결합 연산자
print(sum2)

temp = input('현재 온도는>>')
print(type(temp))

temp2 = float(temp)
print(type(temp2))

if temp2 > 20:
    print('너무 더워요')
else:
    print('아직 안 더워요')

#타입을 변경하는 것: 형변환(casting, 캐스팅)
# 문자로 변경하는 것:str()
# 정수로 변경하는 것: int()
# 실수로 변경하는 것: float()

#문자
#String을 의미, char를 포함하는 의미!
company = '메가'
print(company, end=' ') #print 후, 마지막에 엔터!적용
print('우리 회사는', company)

#논리
food = True #False
food2 = 1 #0

#비교 연산자 ==
if food == food2:
    print('배가 부르시겠군요!')
else:
    print('배가 고파요!')