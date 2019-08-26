# tkinter 라이브러리 import
from tkinter import *

def calc(event):
    label.config(text="계산결과: " + str(eval(entry.get())))
    
# tk 객체 인스턴스 생성하기
window = Tk()
window.title("대중교통 요금 계산하기")
window.geometry("640x480+100+100")
window.resizable(False, False)

# 레이블 생성
label = Label(window, text="연령대 요금 (어린이:450 |청소년 :720 | 성인:1250) / 잔액 // 이동경로(한번:1 |왕복:2)")
label.pack()
label = Label(window, text="0")
label.pack()

# Entry 생성
entry = Entry(window, width=30)
entry.bind("<Return>", calc)
entry.pack()

# 메인 화면 표시
window.mainloop()

  
    else :
      print("1,2으로 다시 선택해주세요.")
    contiue
s = User()
s.set_age()
s.set_money()
s.set_time()
s.set_movenum()