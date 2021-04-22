class Day:
    # 실제값 변수: 인스턴스 변수(동적 변수) <-> 정적변수(static)
    work = None
    time = None
    place = None
    count = 0

    #생성자는 객체 생성될때 생성되는 고유한 실제값이므로 static변수는 안들어감
    def __init__(self, work, time, place):
        self.work = work
        self.time = time
        self. place = place
        Day.count += 1
        print(str(Day.count) + '개 객체가 생성됨')

    def study(self):
        return self.work + '를' + str(self.time) + '시간 하다'
    def where(self):
        return self.place + '에서' + self.work + '를 하다'
    def __str__(self):
        return  self.work + ', ' + str(self.time) + ', ' + self.place


if __name__ == '__main__':
    day1 = Day('파이선공부',10,'강남')
    day2 = Day('자바공부', 11, '신촌')
    day3 = Day('db공부', 12, '종로')
    print(day1)
    print(day2)
    print(day3)
    print(day1.study())
    print(day1.where())