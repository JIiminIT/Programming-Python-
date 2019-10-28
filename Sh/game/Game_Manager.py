from tictactoc import TicTacToe

class GameManager:
    def __int__(self):
        self.ttt = TicTacToe()

    def play(self):
        self.ttt(1,1)
        print(self.ttt)


if __name__ == ' __main__':
    gm = GameManager()
    gm.play()
