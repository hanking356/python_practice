from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class WomanDay(Person, my.Day):
#파이썬 :클래스간 다중 상속이 가능하다.
#자바 : 클래스간 단일산속만 가능하다

#day 생성자는 파라메터가 있는 생성자이므로 상속 받아 객체 생성할때는 생성자 정의를 해줘야 함
    def __init__(self, work, time, place):
        # 다중 상속이므로 Super.이 아니마 my.Day를 써줘야 함
        my.Day.__init__(self, work, time, place)

    def free(self):
        print('쉬다!')

    def __str__(self):
        return self.work + ', ' + str(self.time) + ', ' + self.place

if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기', 20, '마포구')
    woman_day1.free()
    woman_day1.eat()
    print(woman_day1)

