from heapq import heappop, heappush
import time

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__} executed in {(t2-t1) * 1000:.4f}ms")
        return res
    return wrapper


class Solution:
    def __init__(self, path: str):
        self.grid, self.dim, self.start, self.end = self.parse(path)
        self.dirs = [-self.dim, 1, self.dim, -1]

    def parse(self, path):
        with open(path, 'r') as f:
            res = []
            s, e = -1, -1
            for line in f.readlines():
                res.append(line.strip())
        m = "".join(res)
        return m, len(res[0]), m.find('S'), m.find('E')
    
    def inBounds(self, pos):
        return pos >= 0 and pos < len(self.grid)

    @timer
    def parcours(self) -> float | int:
        visite: dict[int, int] = {self.start: 0}
        doing = []
        heappush(doing, (0, self.start))

        maxi = float("inf")
        while doing:
            dist, pos = heappop(doing)

            if dist > maxi:
                break

            if pos == self.end:
                maxi = dist

            for d in self.dirs:
                if (pos - 1) % self.dim == self.dim - 1 and d == -1: continue
                if (pos + 1) % self.dim == 0 and d == 1: continue
                if not self.inBounds(pos+d) or self.grid[pos + d] == '#': continue
                if pos+d not in visite: 
                    heappush(doing, (dist+1, pos+d))
                    visite[pos+d] = dist + 1
        return visite
    
    def manhattan(self, pos1, pos2):
        return abs(pos1 // self.dim - pos2 // self.dim) + abs(pos1 % self.dim - pos2 % self.dim)

    @timer
    def partie12(self):
        visite = self.parcours()
        cpt1, cpt2 = 0, 0
        print(len(visite))
        for pos1 in visite:
            for pos2 in visite:
                if visite[pos2] >= visite[pos1]: continue
                d = self.manhattan(pos1, pos2)
                if d <= 20:
                    if visite[pos1] - visite[pos2] - d+2 > 100: cpt2 += 1
                if d == 2:
                    if visite[pos1] - visite[pos2] > 100: cpt1 += 1
        return cpt1, cpt2


if __name__ == '__main__':
    s = Solution("jour20.txt")
    p1, p2 = s.partie12()
    print(p1, p2)
    assert p1 == 1346
    assert p2 == 985482
