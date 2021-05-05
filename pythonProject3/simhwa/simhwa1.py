from tkinter import *
import threading
import time
import random
# 스레드 클래스
class Thread:
    car = None
    thread = None
    def __init__(self, w,img,x1,y1): #생성자(입력파라메터)
        # 이미지 할당
        self.car = Label(w)
        icon = PhotoImage(file = img) #PhotoImage 클래스를 통해 img(carimage1.png)를 읽음
        self.car.configure(image = icon) #Label을 icon으로 변경
        self.car.image = icon #자동차의 이미지에 위에서 정의한 icon을 저장
        # 스레드 설정
        # threading.Thread() 함수를 호출하여 Thread 객체 생성
        # run은 쓰레드가 실행할 함수 명
        # car, name, x1, y1은 run 함수의 입력 파라메터
        self.thread = threading.Thread(target = self.run, args=(self.car,x1,y1))
        self.thread.start()
    # 스레드 실행 함수
    def run(self, car,x1,y1):
        speed = 0
        while True:
            speed = random.randrange(10,50) # 한 번에 10~50 사이로 움직임
            # 골인지점 x1=500
            if x1 >= 500: # 골인 지점
                break
            x1 = x1 + speed #x1의 위치는 speed값의 누적
            self.car.place(x=x1,y=y1)
            time.sleep(0.5) # 대기시간, 0.5초 마다 메서드가 실행
# 자동차 배치
def Cars():
    # 창, 파일명, x좌표, y좌표
    car1 = Thread(w,'carimage1.png',10,70)
    car2 = Thread(w,'carimage2.png',10,180)
    car3 = Thread(w,'carimage3.png',10,300)
# 메인코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk()
    w.title('자동자 경주') #윈도우창 제목
    w.geometry('500x400') #윈도우창 크기
    # 버튼 배치
    #경기 시작 버튼을 누르면 Cars메서드를 실행
    startbutton = Button(w,text='경기 시작', command=Cars)
    # 위젯이름.pack(파라미터1, 파라미터2, ....), 윈도우 창에 표시할 위젯의 배치 속성
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3,padx=5, pady=5)
    #윈도우에서 이벤트 발생 유지 함수
    w.mainloop()