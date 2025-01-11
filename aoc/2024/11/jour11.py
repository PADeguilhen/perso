from functools import cache

class Solution:
    def __init__(self, path: str):
        self.inp = [i for i in open(path, 'r').read().split(' ')]

    def partie1(self):
        return self.solution(25)

    def partie2(self):
        return self.solution(75)

    @cache
    def solution(self, depth: int):
        cpt = 0
        for a in self.inp:
            cpt += self.solve(a, depth)
        return cpt

    @cache
    def solve(self, a: str, depth: int) -> int:
        if depth == 0:
            return 1
        elif a == '0':
            return self.solve('1', depth - 1)
        elif a == '1':
            return self.solve('2024', (depth - 1))
        elif len(a) % 2 == 0:
            return self.solve(a[:len(a)//2], depth - 1) + self.solve(str(int(a[len(a)//2:])), depth - 1)
        else:
            return self.solve(str(int(a) * 2024), depth - 1)

if __name__ == "__main__":
    s = Solution("jour11.txt")
    print(s.partie1())
    print(s.partie2())
    assert s.partie1() == 182081
    assert s.partie2() == 216318908621637