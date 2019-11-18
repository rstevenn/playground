import random as rd
import numpy as np

class Game:
    def __init__(self):
        self.turn = 0
        self.table = np.zeros((3, 3))
        self.player_turn = rd.randint(1, 2)

    def play(self):
        print("Player %d turn:" % self.player_turn)
        self.print()

        out = input("Player action with format: 'x,y' without space -> ")

        # split the output
        out = out.split(',')
        x, y = int(out[0]), int(out[1])

        # check validiti
        if 0 < x < 4 and 0 < y < 4 and self.table[x-1][y-1] == 0:
            self.table[x-1][y-1] = self.player_turn
        else:
            print("Illegal play")

        # next player
        self.player_turn = 1 if self.player_turn == 2 else 2

        # check if finished
        out = self.is_win()
        if out != 0:
            print("Player %d win" %out)
            self.print()
            return out

        self.turn += 1

    def is_win(self):
        for k in range(3):
            # vertical
            if self.table[k][0] == self.table[k][1] == self.table[k][2] and self.table[k][0] != 0:
                return self.table[k][0]

            # horizontal
            if self.table[0][k] == self.table[1][k] == self.table[2][k] and self.table[0][k] != 0:
                return self.table[0][k]

        if self.table[0][0] == self.table[1][1] == self.table[2][2] and self.table[0][0] != 0:
            return self.table[0][0]
        
        if self.table[0][2] == self.table[1][1] == self.table[2][2] and self.table[2][0] != 0:
            return self.table[0][2]

        return 0

    def run(self):
        while True:
            if self.play() is not None:
                return

    def print(self):

        print("turn %d:\n  1 2 3" %self.turn)
        for j in range(3):
            line = "%d " %(j+1)

            for i in range(3):
                if self.table[i][j] == 0:
                    line += "  "

                elif self.table[i][j] == 1:
                    line += "x "

                elif self.table[i][j] == 2:
                    line += "o "

            print(line)

        print("")


Game().run()
