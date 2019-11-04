from tictactoc import TicTacToe

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
