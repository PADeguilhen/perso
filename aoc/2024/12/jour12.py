from dataclasses import dataclass

@dataclass
class Plot:
    color: str
    area: int
    perimiter: int

class Solution:
    def __init__(self, path: str):
        self.inp = [[elm for elm in line[:-1]] for line in open(path, 'r').readlines()]
        self.visited = [[False for _ in line] for line in self.inp]

    def inBounds(self, l: int, c: int):
        return l >= 0 and c >= 0 and l<len(self.inp) and c<len(self.inp[0])

    def wfs(self, l0: int, c0: int, plot: Plot):
        todo: list[tuple[int, int]] = []
        self.past: set[tuple[int, int]] = set()
        todo.append((l0, c0))

        while len(todo) != 0:
            l, c = todo.pop()
            if (l, c) in self.past: continue
            self.past.add((l, c))

            if not self.inBounds(l, c) or self.inp[l][c] != plot.color:
                self.past.discard((l, c))
                plot.perimiter += 1
                continue

            self.visited[l][c] = True
            plot.area += 1

            if not (l+1, c) in self.past: todo.append((l+1, c))
            if not (l-1, c) in self.past: todo.append((l-1, c))
            if not (l, c+1) in self.past: todo.append((l, c+1))
            if not (l, c-1) in self.past: todo.append((l, c-1))
        return plot

    def partie12(self):
        score1 = 0
        score2 = 0
        for l, line in enumerate(self.inp):
            for c, elm in enumerate(line):
                if self.visited[l][c]:
                    continue
                plot = Plot(elm, 0, 0)
                self.wfs(l, c, plot)
                score2 += plot.area * self.numSides()
                score1 += plot.area * plot.perimiter
        return score1, score2

    def numSides(self):
        visited = set()
        sides = 0
        for (x, y) in self.past:
            for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tx = x + nx
                ty = y + ny
                if (tx, ty) not in self.past:
                    cx, cy = x, y
                    while (cx + ny, cy + nx) in self.past and (cx + nx, cy + ny) not in self.past:
                        cx += ny
                        cy += nx
                    if (cx, cy, nx, ny) not in visited:
                        visited.add((cx, cy, nx, ny))
                        sides += 1
        return sides

if __name__ == "__main__":
    s = Solution("jour12.txt")
    print(s.partie12())


    p1, p2 = Solution("jour12.txt").partie12()
    assert p1 == 1363484
    assert p2 == 838988