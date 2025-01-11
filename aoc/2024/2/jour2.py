class Solution:
    def __init__(self, path: str) -> None:
        self.lines = [[int(j) for j in i.split(' ')] for i in open(path ,'r').readlines()]
    
    def isSafe(self, incr, n, nPlus):
        if incr:
            return 0 < nPlus - n <= 3
        else:
            return 0 < n - nPlus <= 3

    def partie1(self, lines = None):
        lines = self.lines if lines == None else lines
        cpt = 0
        for line in lines:
            incr = line[0] < line[1]
            for i, n in enumerate(line[:-1]):
                if not self.isSafe(incr, n, line[i+1]):
                    break
            else:
                cpt += 1
        return cpt

    def partie2(self):
        cpt = 0
        for line in self.lines:
            test = self.partie1([line[:i] + line[i+1:] for i, _ in enumerate(line)])
            if test > 0:
                cpt += 1
        return cpt

if __name__ == "__main__":
    s = Solution("jour2.txt")
    print(s.partie1())
    print(s.partie2())
    assert s.partie1() == 442
    assert s.partie2() == 493
