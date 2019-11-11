#2301 강지민
#본인의 퍼스널 컬러를 간단하고 금전적인 부담없이 가볍게 검사할 수 있는 테스터기 입니다.
#실행은 메인에서 하면 됩니다.

import tkinter as tk
import sys

class Main:
    window = tk.Tk()

    answer = ''

    window.title('Personal Color')
    window.geometry('800x700+100+100')
    window.resizable(False, False)

#출력 내용
    springwarm = '봄 웜톤 입니다.\n봄 타입은 화사하고 따뜻한 카멜, 복숭아, 황금 노랑 등의 색이 가장 잘 어울립니다. 여기에 밝은 빨강으로 포인트를 줄 수 있습니다. 가장 피해야 할 것은 어둡고 칙칙한 색입니다. 특히 흑백의 조합은 어울리지 않는 색입니다. 자주색이 부담스럽다면 양말부터 시작해보는 건 어떨까요?'
    fallwarm = '가을웜톤 입니다.+\n+ 가을 타입은 톤 다운된 황금계열 위주로 입는 것이 좋습니다. 주로 카멜, 베이지, 오렌지, 짙은 갈색 등이 어울리고, 파란 계열보다는 청록색으로 포인트를 주는 것이 잘 어울립니다. 베이지색 바지를 입었다면 청록색 스웨터 혹은 캐주얼 셔츠를 입어보세요.'
    summercool = '여름쿨톤입니다.+\n + 여름 타입은 전체적으로 파스텔톤과 톤 다운된 장미색과 파란색이 어울립니다. 라벤더, 회갈색, 흐린 하늘색 위주로 입되 검은색과 주황색은 피하는 것이 좋다고 합니다. 밋밋한 하얀 와이셔츠보다 밝은 하늘색 혹은 연한 보라색 와이셔츠를 장만해보는 것은 어떨까요?'
    wintercool = '겨울쿨톤입니다 +\n+ 겨울 타입은 채도가 높고 쨍한 느낌의 색이 어울립니다. 대표적으로 검은색, 흰색, 남색과 빨강 그리고 핫핑크가 겨울 타입 피부색에 잘 어울립니다. 좀 더 연한 색으로는 파스텔 계열보다 더 흰색이 많이 들어간 밝은 컬러(Icy color)를 활용해 보세요.'

    def __init__(self):

        # self.acnt = 0
        # self.bcnt = 0
        # self.ccnt = 0
        # self.dcnt = 0
        self.a=0
        self.b=0
        self.c=0
        self.d=0

        self.label = tk.Label(self.window, text='Personal Color')
        self.label.pack()

        self.skin()

        self.window.mainloop()

#라디오 파티..
#모든 라디오를 생성할때 각 버튼에 맞는 variable과 command  value값을 넣어 구분함
    def skin(self):
    #첫번째 질문
        self.question_1 = tk.IntVar()
        self.label = tk.Label(self.window, text="1. 자신의 피부색은?")
        self.label.pack()
        radio1 = tk.Radiobutton(self.window, text="A.내 피부가 노란편이다.", variable=self.question_1, command=self.hair, value=1)
        radio1.pack()
        radio2 = tk.Radiobutton(self.window, text="B.내 피부가 붉은편이다.", variable=self.question_1, command=self.hair, value=2)
        radio2.pack()
    #두번째 질문
    def hair(self):
        self.question_2 = tk.IntVar()
        self.label = tk.Label(self.window, text="2. 자신의 머리카락 색은?")
        self.label.pack()
        radio3 = tk.Radiobutton(self.window, text="A.밝은 갈색", variable=self.question_2, command=self.eye, value=1)
        radio3.pack()

        radio4 = tk.Radiobutton(self.window, text="B.소프트한 검정", variable=self.question_2, command=self.eye, value=2)
        radio4.pack()

        radio5 = tk.Radiobutton(self.window, text="C.어두운 갈색", variable=self.question_2, command=self.eye, value=3)
        radio5.pack()

        radio6 = tk.Radiobutton(self.window, text="D.새까만 검정", variable=self.question_2, command=self.eye, value=4)
        radio6.pack()
    #세번째 질문
    def eye(self):
        self.question_3 = tk.IntVar()
        self.label = tk.Label(self.window, text="3. 자신의 눈동자 색은?")
        self.label.pack()

        radio7 = tk.Radiobutton(self.window, text="A.밝은 갈색", variable=self.question_3, command=self.lip, value=1)
        radio7.pack()

        radio8 = tk.Radiobutton(self.window, text="B.소프트한 검정", variable=self.question_3, command=self.lip, value=2)
        radio8.pack()

        radio9 = tk.Radiobutton(self.window, text="C.어두운 갈색", variable=self.question_3, command=self.lip, value=3)
        radio9.pack()

        radio10 = tk.Radiobutton(self.window, text="D.새까만 검정", variable=self.question_3, command=self.lip, value=4)
        radio10.pack()
#4번쩨 질문
    def lip(self):
        self.question_4 = tk.IntVar()
        self.question_5 = tk.IntVar()
        self.label = tk.Label(self.window, text="4. 자신에게 잘 어울리는 립스틱 색은?")
        self.label.pack()

        radio11 = tk.Radiobutton(self.window, text="A.피치핑크", variable=self.question_4, command=self.jewelry, value=1)
        radio11.pack()

        radio12 = tk.Radiobutton(self.window, text="B.로즈핑크", variable=self.question_4, command=self.jewelry, value=2)
        radio12.pack()

        radio13 = tk.Radiobutton(self.window, text="C.샐먼핑크", variable=self.question_4, command=self.jewelry, value=3)
        radio13.pack()

        radio14 = tk.Radiobutton(self.window, text="D.마젠타", variable=self.question_4, command=self.jewelry, value=4)
        radio14.pack()
    #5번째 질문
    def jewelry(self):
        self.label = tk.Label(self.window, text="5. 자신에게 잘 어울리는 쥬얼리 색은?")
        self.label.pack()

        radio15 = tk.Radiobutton(self.window, text="A.골드 쥬얼리", variable=self.question_5, command=self.result, value=1)
        radio15.pack()

        radio16 = tk.Radiobutton(self.window, text="C.실버 쥬얼리", variable=self.question_5, command=self.result, value=2)
        radio16.pack()

    # def checkA(self):
    #     self.acnt += 1
    #
    # def checkB(self):
    #     self.bcnt += 1
    #
    # def checkC(self):
    #     self.ccnt += 1
    #
    # def checkD(self):
    #     self.dcnt += 1


#선택한거 나오게함
    def result(self):
        self.a = str(self.question_1.get())
        self.b = str(self.question_2.get())
        self.c = str(self.question_3.get())
        self.d = str(self.question_4.get())
        print("RadioVariety_1 = " + self.a + "\n" +
              "RadioVariety_2 = " + self.b + "\n" +
              "RadioVariety_3 = " + self.c + "\n" +
              "RadioVariety_4 = " + self.d + "\n"  )
        self.comparison()

#버튼마다 값을 비교하기 위해 배열을 생성함.
    def comparison(self):
        comparison = [int(self.a), int(self.b), int(self.c), int(self.d)]
#if문으로 비교하면서 선택한 값에 따라 결과값의 춫ㄹ력이 달라지게함.
        if comparison[0] == 1 or comparison[0] == 3 and comparison[1] == 1 and comparison[2] == 1 and comparison[3] == 1 or comparison[3] ==3 :
            self.answer = self.springwarm
        elif comparison[0] == 2 or comparison[0] == 4 and comparison[1] == 2 and comparison[2] == 2 and comparison[3] == 2 or comparison[3] == 4:
            self.answer = self.summercool
        elif comparison[0] == 1 or comparison[0] == 3 and comparison[1] == 3 or comparison[1] == 3 and comparison[2] == 3 and comparison[3] == 1:
            self.answer = self.fallwarm
        elif comparison[0] == 2 or comparison[0] == 4 and comparison[1] == 4 and comparison[2] == 4 and comparison[3] == 4 or comparison[3] ==2 :
            self.answer = self.wintercool

        print(self.answer)

#결과 값이 txt파일로 들어갑니다.
        try:
            with open("output.txt", mode='w', encoding='utf-8') as f:
                f.write(self.answer)
        except:
            print("Error: 파일 쓰기 에러")
            sys.exit(1)

if __name__ == '__main__':
    Main()