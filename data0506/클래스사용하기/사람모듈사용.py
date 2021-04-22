from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

day5 = my.Day('놀기', 10, '영등포')
print(day5)

super_man = SuperMan()
super_man.name = '클라크'
super_man.age = 1000
super_man.speed = 1
super_man.fly = True
print(super_man)
super_man.eat()
super_man.run()
super_man.sky()


