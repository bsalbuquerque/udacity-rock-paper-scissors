#!/usr/bin/env python3

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0
        self.self_moves = []
        self.enemy_moves = []

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        print("Write 'quit' to end the game")
        self.choice = str(input("Rock, paper, scissors? "))
        if self.choice.lower() not in moves and self.choice.lower() != "quit":
            return self.move()
        return self.choice.lower()


class ReflectPlayer(Player):
    def move(self):
        if len(self.enemy_moves) == 0:
            return random.choice(moves)
        return self.enemy_moves[-1]

    def learn(self, my_move, their_move):
        self.self_moves.append(my_move)
        self.enemy_moves.append(their_move)


class CyclePlayer(Player):
    def move(self):
        if len(self.self_moves) == 0:
            return random.choice(moves)
        elif moves.index(self.self_moves[-1]) == 2:
            return moves[0]
        else:
            self.new_position = moves.index(self.self_moves[-1]) + 1
            return moves[self.new_position]


class Game:
    def __init__(self, p1, p2):
        self.round = 1
        self.quit = False
        self.p1 = p1
        self.p2 = p2

    def play_game(self):
        print("Rock Paper Scissor, Go!\n")
        while self.quit is False:
            self.play_round()

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        print(f"Round {self.round} --")
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.p1.choice != "quit":
            print(f"Player 1: {move1}," +
                  f"Player 2: {move2}")
            if move1 == move2:
                print("** TIE **")
            elif self.beats(move1, move2):
                print("** PLAYER ONE WINS **")
                self.p1.score += 1
            else:
                print("** PLAYER TWO WINS **")
                self.p2.score += 1
            print(f"Score: Player One {self.p1.score}," +
                  f"Player Two {self.p2.score}\n")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            self.round += 1
        else:
            self.end_game()

    def end_game(self):
        self.quit = True
        print("Game Over!")
        if self.p1.score > self.p2.score:
            print("Player One is the WINNER!")
        elif self.p1.score < self.p2.score:
            print("Player Two is the WINNER!")
        else:
            print("We have a TIE!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
