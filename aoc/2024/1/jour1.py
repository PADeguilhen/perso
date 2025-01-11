class Solution:
    def __init__(self, path: str):
        self.left, self.right, self.inp = self.parse(path)
    
    def parse(self, path: int):
        left, right, inp = [], [], []
        with open(path, 'r') as file:
            for line in file:
                tmp = line.split('   ')
                l, r = int(tmp[0]), int(tmp[1])
                left.append(l)
                right.append(r)

        left.sort()
        right.sort()
        inp = zip(left, right)
        return left, right, inp

    def partie1(self):
        
        sum = 0
        for (x, y) in self.inp:
            sum += abs(x - y)
        return sum

    def partie2(self): # imagine making a 0(n) solution... couldn't be me.
        sum = 0
        for l in self.left:
            sum += l * self.right.count(l)
        return sum

if __name__ == "__main__":
    s = Solution("jour1.txt")
    print(s.partie1())
    print(s.partie2())
    assert s.partie1() == 2344935
    assert s.partie2() == 27647262
