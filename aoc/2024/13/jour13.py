import re

class Solution:
    def __init__(self, path: str):
        self.inp: list[tuple[int, int, int]] = self.parse(path)
    
    def parse(self, path: str):
        res = []
        lines = open(path, 'r').readlines()
        for l, line in enumerate(lines[::4]):
            ax, ay = re.findall(r"\d+", line)
            bx, by = re.findall(r"\d+", lines[l*4+1])
            tx, ty = re.findall(r"\d+", lines[l*4+2])
            res.append(((int(ax), int(ay)), (int(bx), int(by)), (int(tx), int(ty))))
        return res

    def partie1(self):
        tokens = 0
        for line in self.inp:
            ax, ay = line[0]
            bx, by = line[1]
            tx, ty = line[2]

            b = (ty * ax - tx * ay) // (ax * by - ay * bx)
            a = (tx - bx * b) // ax

            if ax * a + b * bx == tx and ay * a + b * by == ty:
                tokens += int(3*a + b)
        return tokens

    def partie2(self):
        tokens = 0
        for line in self.inp:
            ax, ay = line[0]
            bx, by = line[1]
            tx, ty = map(lambda x: x + 10_000_000_000_000, line[2])

            b = (ty * ax - tx * ay) // (ax * by - ay * bx)
            a = (tx - bx * b) // ax

            if ax * a + b * bx == tx and ay * a + b * by == ty:
                tokens += int(3*a + b)
        return tokens



if __name__ == "__main__":
    s = Solution("jour13.txt")
    assert s.partie1() == 31897
    assert s.partie2() == 87596249540359