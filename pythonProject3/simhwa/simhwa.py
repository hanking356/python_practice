from tkinter import *
import threading
import time
import random
# 스레드 실행 클래스
class Thread:
    car = None
    thread = None
    def __init__(self, w,name,x1,y1):
        # 레이블
        #window 창 열기
        self.car = Label(w,text=name)
        # 스레드 설정
        # threading.Thread() 함수를 호출하여 Thread 객체 생성
        # run은 쓰레드가 실행할 함수 명
        # car, name, x1, y1은 run 함수의 입력 파라메터
        self.thread = threading.Thread(target = self.run, args=(self.car,name,x1,y1))
        #Thread 객체의 start() 메서드 호출
        self.thread.start()
    # 스레드 실행 함수
    def run(self, car,name,x1,y1):
        speed = 0
        while True:
            speed = random.randrange(10,50) # 한 번에 10~50 사이로 움직임
            # 골인지점 x1=450
            if x1 >= 450: # 최대값
                self.car.config(text=name + ' 골인', fg='red') # 최대값 도달시 텍스트 변경
                break
            x1 = x1 + speed #x1의 위치는 speed값의 누적
            self.car.place(x=x1,y=y1)
            time.sleep(0.5) # 대기 시간, 0.5초 마다 메서드가 실행
# 자동차 배치
def Cars():
    # 창, 텍스트, x좌표, y좌표
    car1 = Thread(w,'자동차1',10,50)
    car2 = Thread(w,'자동차2',10,100)
    car3 = Thread(w,'자동차3',10,150)
# 메인코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk()
    w.title('자동자 경주') #윈도우창 제목
    w.geometry('500x200') #윈도우창 크기
    # 버튼 배치
    startbutton = Button(w,text='경기 시작', command=Cars)
    #위젯이름.pack(파라미터1, 파라미터2, ....), 윈도우 창에 표시할 위젯의 배치 속성
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3,padx=5, pady=5)
    #윈도우에서 이벤트 발생 유지 함수
    w.mainloop()