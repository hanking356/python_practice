class Truck:
    weight = None
    company = None

    def move(self):
        print(self.weight, '톤의 짐을 실어나르다.')
    def own(self):
        print(self.company, '회사 소속의 트럭입니다.')

    def __str__(self):
        return str(self.weight) + ', ' + self.company

if __name__ == '__main__':
    truck2 = Truck()
    truck2.weight = 1
    truck2.company = '메가'

    print(truck2)
    print(truck2.weight)
    print(truck2.company)
    truck2.move()
    truck2.own()