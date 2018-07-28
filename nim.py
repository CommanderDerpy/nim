from enum import Enum


class Player(Enum):
    NOBODY = 1
    PLAYER = 2
    AI = 3


class Nim:
    balls = 12
    winner = Player.NOBODY
    curTurn = Player.AI

    def start(self):
        while self.winner == Player.NOBODY:
            self.ai_turn()
            if not self.check_for_winner():
                self.player_turn()
                self.check_for_winner()

    def ai_turn(self):
        self.curTurn = Player.AI
        self.take_x_balls(1)
        print("AI turn and takes a ball! " + str(self.balls))

    def player_turn(self):
        self.curTurn = Player.PLAYER
        self.take_x_balls(1)
        print("Player turn and takes a ball! " + str(self.balls))

    def check_for_winner(self):
        if self.balls == 0:
            if self.curTurn == Player.AI:
                self.winner = Player.AI
            else:
                self.winner = Player.PLAYER
            return True

        else:
            return False

    def take_x_balls(self, x):
        self.balls -= x

    def tell_winner(self):
        print("The winner is: " + str(self.winner))
