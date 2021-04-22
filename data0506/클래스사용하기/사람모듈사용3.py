from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class Student(Person):
    def study(self):
        print('공부하다')
class Worker(Person):
    company = None
    def work(self):
        print('일하다')

    def __str__(self):
        return self.name + '' + str(self.age) + self.company
if __name__ == '__main__':
    student = Student()
    student.name = '홍길동'
    student.age = 100
    print(student)
    student.study()

    worker = Worker()
    worker.age = 200
    worker.name = '송길동'
    worker.company = '메가'
    print(worker)
    worker.work()