from collections import deque
from itertools import count
from itertools import cycle

class Sim:

    def __init__(self, players, last_marble):
        self.players = [0] * players
        self.current_marble = 0
        self.last_marble = last_marble
        self.marbles = deque([0])

    def place_marbles(self):
        for m, p_index in enumerate(cycle(range(len(self.players)))):
            m += 1
            if m == self.last_marble:
                return
            if m % 23 == 0:
                self.marbles.rotate(7)
                self.players[p_index] += m + self.marbles.pop()
                self.marbles.rotate(-1)
            else:
                self.marbles.rotate(-1)
                self.marbles.append(m)

def solve(puzzle):
    players = puzzle[0]

def get_input():
    return open('puzzle_input.txt').read()[:-1].split(' ')

if __name__ == "__main__":
    puzzle = get_input()
    s = Sim(int(puzzle[0]), (int(puzzle[6]) + 1) * 100)
    print(s.last_marble)
    s.place_marbles()
    print(max(s.players))
