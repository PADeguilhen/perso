from heapq import heappop, heappush

class Solution:
    def __init__(self, path: str, length=70, num=1024):
        self.dim = length + 1
        self.size = (self.dim) ** 2
        self.wall = set()
        self.other = []
        with open(path, 'r') as f:
            for _ in range(num):
                a, b = f.readline().split(',')
                self.wall.add(int(a) + int(b.strip()) * (self.dim))
            for line in f.readlines():
                a, b = line.split(',')
                self.other.append(int(a) + int(b.strip()) * (self.dim))
        self.dirs = [-self.dim, 1, self.dim, -1]

    def inBounds(self, pos):
        return pos >= 0 and pos < self.size

    def partie1(self):
        return self.parcours()
    
    def parcours(self):
        visite = set()
        doing = []
        heappush(doing, (0, 0))
        maxi = float("inf")
        while doing:
            dist, pos = heappop(doing)

            if dist > maxi:
                continue

            if pos == self.size - 1:
                maxi = dist

            for d in self.dirs:
                if (pos - 1) % self.dim == self.dim - 1 and d == -1: continue
                if (pos + 1) % self.dim == 0 and d == 1: continue
                if not self.inBounds(pos+d) or pos + d in self.wall: continue
                if pos+d not in visite: heappush(doing, (dist+1, pos+d))
                visite.add(pos+d)
        return maxi
    
    def partie2(self):
        l, r = 0, len(self.other)
        old = self.wall.copy()
        bestInf = -1
        while l<=r:
            m = (l+r)//2
            self.wall = old | set(self.other[:m+1])
            if self.parcours() == float("inf"):
                bestInf = self.other[m]
                r = m - 1
            else:
                l = m + 1
        return (bestInf%self.dim, bestInf//self.dim)


if __name__ == "__main__":
    s = Solution("jour18.txt")
    p1 = s.partie1()
    print(p1)
    p2 = s.partie2()
    print(p2)
    assert p1 == 272
    assert p2 == (16, 44)

