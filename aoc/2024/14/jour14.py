from dataclasses import dataclass

@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]
    
    def move(self, width, hight, times):
        self.position = (
            (self.position[0] + self.velocity[0] * times) % width,
            (self.position[1] + self.velocity[1] * times) % hight
        )
    
    def __hash__(self):
        return hash(self.position)


class Solution:
    def __init__(self, path: str):
        self.path = path
        self.robots: list[Robot] = self.parse(path)
        self.width = 101
        self.hight = 103
    
    def parse(self, path):
        inp = open(path, 'r').readlines()
        rob: list[Robot] = []
        for line in inp:
            l1, l2 = line.split(' ')
            p1, p2 = l1.split(',')
            v1, v2 = l2.split(',')
            rob.append(Robot(
                (int(p1[2:]), int(p2)),
                (int(v1[2:]), int(v2))
            ))
        return rob
    
    def moving(self, depth=100):
        for rob in self.robots:
            rob.move(self.width, self.hight, depth)
    
    def partie1(self):
        self.moving()
        q1, q2, q3, q4 = 0, 0, 0, 0
        for rob in self.robots:
            c, l = rob.position
            if c < self.width//2 and l < self.hight//2: q1 += 1
            elif c < self.width//2 and self.hight//2 < l: q2 += 1
            elif self.width//2 < c and l < self.hight//2: q3 += 1
            elif self.width//2 < c and self.hight//2 < l: q4 += 1
        self.robots = self.parse(self.path)
        return q1 * q2 * q3 * q4

    def partie2(self):
        cpt = 0
        while self.overlap():
            cpt += 1
            self.moving(depth=1)
        return cpt
    
    def overlap(self):
        s = set()
        for rob in self.robots:
            if rob.position in s:
                return True
            s.add(rob.position)
        return False

    def __repr__(self):
        dic: dict[tuple[int, int], int] = {}
        for rob in self.robots:
            try:
                dic[rob.position] += 1
            except:
                dic[rob.position] = 1

        out = ''
        for l in range(self.hight):
            for c in range(self.width):
                try:
                    out += str(dic[(c, l)]) + ' '
                except:
                    out += '  '
            out += '\n'
        return out

if __name__ == "__main__":
    s = Solution("jour14.txt")
    print("partie 1:", s.partie1())
    print("partie 2:", s.partie2())
