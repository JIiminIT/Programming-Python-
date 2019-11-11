from tictactoc import TicTacToe
import math


class GameManager:
    def __int__(self):
        self.ttt = TicTacToe()

def play(self):
    print(self.ttt)
    while True:
        self.ttt(1,1)
        print(self.ttt)
        row = int(input('row : '))
        col = int(input('col : '))
        self.ttt.set(row,col)
        print(self.ttt)
        if self.ttt.check_winner() =='o':
            print("o win !!")
            break
        elif self.ttt_winner() == 'X':
            print("x !!")
            break
        elif self.ttt_winner() == 'd':
            print("무승부")
            break


if __name__ == ' __main__':
    gm = GameManager()
    gm.play()


class Game_Manager_GUI:
    def __init__(self):
        self.ttt = TicTacToe()
        CANVAS_SIZE = 100
        self.TITLE_SIZE = CANVAS_SIZE /3
        print(set.ttt)

        self.root = tkinter.Tk()
        self.root =('틱택토')
        self.root.geometry(str(CANVAS_SIZE) + 'x'+str)

        self.images = dict()
        self.images['o'] = tkinter.PhotoImage(file = 'img/o.git')

        self.canvas,bind("<Button-li", self.clike_Handiler) #버튼을 누르면 clike handiler 가 실행된다.

        if self.ttt.check.winner() == "o":
            messagebox.sgiwubfi("d아러 아아나ㅓ렁ㅇ나","o win")

        elif self.ttt.check_winner() == "X":
            messagebox.sgiwubfi("d아러 아아나ㅓ렁ㅇ나", "o win")

        def draw_board(self):
            ackear
            self..canvas.delete('all')

            x =0
            y =0
            for i, y in enmerate(self.ttt.board):
                if v -- :,
;               pass
                elif v = "o":
    self.cabvas,create_image(x,y, ancgir:bwdlfjk)

    if i % 3 ==:
        x=0
        y +=self.TITLE_SIZE


    def click_handerlier(self, event):
        pass

    def play(self):
        pass

if __name__ == '__main__':
    gm.GameManager_GUI()
    gm.play()