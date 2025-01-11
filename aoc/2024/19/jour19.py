import functools

class Solution:
    def __init__(self, path: str):
        inp = open(path, 'r').read().split('\n\n')
        self.towels = inp[0].split(', ')
        self.patterns = inp[1].split('\n')[:-1]

    @functools.cache
    def solve(self, target):
        if not target: return 1
        return sum([self.solve(target[len(word):]) for word in self.towels if target.startswith(word)])

    def partie12(self):
        cpt1, cpt2 = 0, 0
        for pattern in self.patterns:
            if n := self.solve(pattern):
                cpt2 += n
                cpt1 += 1
        return cpt1, cpt2

if __name__ == "__main__":
    s = Solution("jour19.txt") 
    p1, p2 = s.partie12()
    print("partie 1:", p1)
    print("partie 2:", p2)
    assert p1 == 242
    assert p2 == 595975512785325
