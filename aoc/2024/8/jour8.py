import cmath
from itertools import combinations

class Solution:
    def __init__(self, path: str):
        self.inp, self.maxx, self.maxy = self.parse(path)

    def parse(self, path: str):
        input = open(path, 'r').readlines()
        maxx = len(input)
        maxy = len(input[0]) - 1
        inp = {}
        out = ""
        for l, line in enumerate(input):
            for c, col in enumerate(line[:-1]):
                if col != '.':
                    try:
                        inp[col].append(l+c*1j)
                    except KeyError:
                        inp[col] = [l+c*1j]
                    out += col
                else:
                    col += ' '
        return inp, maxx, maxy

    def inBounds(self, c: complex):
        return 0 <= c.real < self.maxx and 0 <= c.imag < self.maxy

    def partie1(self):
        s = set()
        for k in self.inp.keys():
            for p1, p2 in list(combinations(self.inp[k], 2)):
                diff = p2 - p1

                if self.inBounds(p2 + diff):
                    s.add(p2 + diff)
                if self.inBounds(p1 - diff):
                    s.add(p1 - diff)
        return len(s)

    def partie2(self):
        s = set()
        for k in self.inp.keys():
            for p1, p2 in list(combinations(self.inp[k], 2)):
                diff = p2 - p1

                n = 0
                f1 = False
                f2 = False
                while True:
                    if self.inBounds(p2 + n * diff):
                        s.add(p2 + n * diff)
                    else:
                        f1 = True
                    if self.inBounds(p1 - n * diff):
                        s.add(p1 - n * diff)
                    else:
                        f2 = True
                    
                    if f1 and f2:
                        break
                    n += 1
        return len(s)

if __name__ == "__main__":
    s = Solution("jour8.txt")
    assert s.partie1() == 361
    assert s.partie2() == 1249
