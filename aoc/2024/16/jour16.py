from heapq import heappop, heappush
import time

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__} executed in {(t2-t1) * 1000}ms")
        return res
    return wrapper

class Solution:
    def __init__(self , path: str):
        lines = [line.strip() for line in open(path, 'r')]
        dx = len(lines[0])
        self.maze = list("".join(lines))
        self.start, self.end = self.maze.index('S'), self.maze.index('E')
        self.dirs = [-dx, 1, dx, -1]

    def parcours(self):
        visited = {}
        doing = []
        self.paths = []
        maxi = float("inf")
        itercpt = 0
        heappush(doing, (0, self.start, 1, ""))
        while doing:
            itercpt += 1
            score, pos, dir, path = heappop(doing)
            if score > maxi:
                continue

            if (pos, dir) in visited and visited[(pos, dir)] < score:
                continue

            visited[(pos, dir)] = score
            if pos == self.end:
                maxi = score
                self.paths.append(path)
            
            if self.maze[pos + self.dirs[dir]] != '#':
                heappush(doing, (score + 1, pos+self.dirs[dir], dir, path + "F"))
            heappush(doing, (score + 1000, pos, (dir+1) % 4, path + "R"))
            heappush(doing, (score + 1000, pos, (dir-1) % 4, path + "L"))
        print(itercpt)
        return maxi

    #@timer
    def partie1(self):
        return self.parcours()

    #@timer
    def partie2(self):
        tiles = set()
        tiles.add(self.start)
        for p in self.paths:
            t, d = (self.start, 1)
            for c in p:
                if c=="L": d=(d-1)%4
                elif c=="R": d=(d+1)%4
                elif c=="F":
                    t+=self.dirs[d]
                    tiles.add(t)
        return len(tiles)
       

if __name__ == "__main__":
    s = Solution("jour16.txt")
    print(s.partie1())
    print(s.partie2())
