class TicTacToe:
    def __int__(self):
        self.board = [",",",",",",",",",",",",",",",",","]
        self.current_turn = "X"

    def set(self,row,col):
        if self.get(row,col) == ".":

        if self.current_turn == "0"
            self.current_turn = "X"
        else:
            self.current_turn = "O"
        self.board[(row * 3) + col] = self.current_turn

    def get(self, row, col):
        return self.board[(row*3) + col]

    def check_winner(self):
        check = self.current_turn
        for i in range(3):
            if self.get(i,0) == self.get(i,1) == self.get(i,2) == check:
                # 수직
                return check
                # 수평
            elif self.get(0,i) == self.get(1,i) == self.get(2,i) == check:
                return check

        if self.get(0,0) == self.geeet(1,i) == self.get(2,2) == check:
            return check
        elif self.get(0,2) == self.get(1,1) == self.get(2,0) == check:
            return check

        if not "." in self.board:
            return "d"

    def __str__(self):
        s = ""

        for i, in enumerate(self.board):
            s += v
            if i % 3 == 2:
                s+= "\n"

        return None