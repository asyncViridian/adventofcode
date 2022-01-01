import re

### PART 1
# read the input into a list
f = open('input/day04.txt', 'r')
fi = [x[:-1] for x in f]
f.close()
# define Board class
class BingoBoard:
    def __init__(self, linestate):
        self.state = [
                [int(i) for i in re.split(r'\s+', l) if len(i.strip())>0]
                for l in linestate
        ]
        self.reverse = {}
        for i in range(5):
            for j in range(5):
                self.reverse[ self.state[i][j] ] = (i,j)
        self.hits = [[0 for _ in range(5)] for _ in range(5)]
    def callNum(self, num):
        if num not in self.reverse:
            return None
        loc = self.reverse[num]
        self.hits[loc[0]][loc[1]] = 1
        # check row win condition
        if sum([self.hits[loc[0]][i] for i in range(5)])==5:
            return self.unmarkedScore() * num
        # check col win condition
        if sum([self.hits[i][loc[1]] for i in range(5)])==5:
            return self.unmarkedScore() * num
    def unmarkedScore(self):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.hits[i][j]==0:
                    score += self.state[i][j]
        return score
# parse input into relevant things
nums = [int(i) for i in fi[0].split(',')]
boards = []
fi = fi[1:]
while len(fi)>0:
    boards.append(BingoBoard(fi[1:6]))
    fi = fi[6:]
# run the bingosim
for num in nums:
    sc = None
    for ib in range(len(boards)):
        sc = boards[ib].callNum(num)
        if sc is not None:
            print(sc)
            break
    if sc is not None:
        break

### PART 2
# TODO
