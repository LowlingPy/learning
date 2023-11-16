# Mahdi Mohammadi khah 982011056

import random
class Game:
    def __init__(self, goal):
        # self.goal = random.randint(-10, 10)  # Khalaqiat
        self.goal = goal
        self.pointer = 0

    def move(self, move):
        if move == 'R':
            self.pointer += 1
        elif move =='L':
            self.pointer += -1
        else:
            print('Wrong move')

    def win(self):
        if self.goal == self.pointer:
            return True
        return False


goal = int(input())
game = Game(goal)
while not game.win():
    move = input()
    game.move(move)
    print(game.pointer)
    print(game.goal)



