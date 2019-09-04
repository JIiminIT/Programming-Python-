from tkinter import *

window = Tk()
window.title("대중교통 이용 요금 계산")
window.geometry("640x480+100+100")
window.resizable(False, False)


lable = Label (window,text = "연령대를 선택해주세요.")

def set_age(self):
    self.age= int(input("나이를 입력해주세요."))
    if self.age <=5:
      self.agemoney = 450
    elif self.age <=19 :
      self.agemoney =  720
    elif self.age < 20:
      self.agemoney = 1250

def set_money(self):
    self.money= int(input("잔액을 입력해주세요."))

def set_movenum(self):
    self.movenum = int(input("이용하시는 번호를 입력해주세요. :   1.한번  / 2. 왕복"))
    if self.movenum == 1:
      result = int(self.money // self.agemoney)
      print(result)
    elif self.movenum ==2:
      result = int(self.money / self.agemoney // 2)
      print(result)


def check():
    label.config(text= "RadioVariety_1 = " + str(agemoney1.get()) + "\n" +
                       "RadioVariety_2 = " + str(agemoney2.get()) + "\n\n" +
                       "Total = "          + str(agemoney1.get() + agemoney2.get() + agemoney3.get()  ))
agemoney1=window.IntVar()
agemoney2=window.IntVar()
agemoney3=window.IntVar()


radio1=window.Radiobutton(window, text="어린이", value=450, variable=agemoney1, command=set_age)
radio1.pack()

radio2=window.Radiobutton(window, text="청소년", value=720, variable=agemoney2, command=set_age)
radio2.pack()

radio3=window.Radiobutton(window, text="성인", value=1250, variable=agemoney3, command=set_age)
radio3.pack()

label=window.Label(window, text="None", height=5)
label.pack()


window.mainloop()