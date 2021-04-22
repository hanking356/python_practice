def exam01(x, y):
    print('아이디가',x,'인',y,'님이 로그인되었습니다')
def exam02(x, y):
    print('숫자1:', x)
    print('숫자2:', y)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

def exam03(x, y):
    print(x,'님의 10년 후의 나이는', y + 10, '세입니다.')

def exam04(x):
    if x>10000:
        print('엄마 너무 용돈이 많아요')
    else:
        print('엄마 너무 용돈이 적어요')

def exam05(x):
    if x //2 == 0:
        print('홀수')
    else:
        print('짝수')
def exam06():
    x = int(input('실적을 입력하세요>>'))
    if x>1000:
        print('축하합니다. 실적을 달성하셨습니다.')
        print('당신의 이번달 보너스는', x*0.2,'만원입니다.')

def exam07(x,y,z):
    print('미사일 이름은:', x)
    print('미사일 시작값은:', y)
    print('미사일 움직이는 값은:', z)
    print('-----------------------------------')
    print('슛 미사일이', y+z,'로 이동되었습니다.' )

def exam08(x,y):
    print('받은 돈:', x)
    print('상품의 총액:', y)
    print('부가세:', y*0.1)
    return x - y

def exam09():
    for i in range(1000):
        print(i, '*')
