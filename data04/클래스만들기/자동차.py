class Car:
    #클래스: 멤버변수(인스턴스변수) + 멤버함수
    speed = None
    color = None

    def run(self):
        print(self.color, '색이 달리다.')
    def start(self):
        print(self.speed, '속도로 출발하다')

    def __str__(self):
        return str(self.speed) + ', ' + self.color

if __name__ == '__main__':
    car1 = Car() #객체생성
    car1.color = '빨강'
    car1.speed = 100
    print(car1)
    print(car1.color)
    print(car1.speed)
    car1.run()
    car1.start()