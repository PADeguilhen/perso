import time

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__} executed in {(t2-t1) * 1000:.4f}ms")
        return res
    return wrapper

class Guard:
    def __init__(self, x: int, y: int, direction: int) -> None:
        self.x = x
        self.y = y
        self.direction = direction
    
    def move(self) -> None:
        if self.direction == 0: # up
            self.x -= 1
        elif self.direction == 1: # left
            self.y -= 1
        elif self.direction == 2: # down
            self.x += 1
        elif self.direction == 3: # right
            self.y += 1
    
    def movepos(self, direction: int = None) -> tuple[int, int]:
        direction = self.direction if direction == None else direction
        match direction:
            case 0:
                return (self.x-1, self.y)
            case 1:
                return (self.x, self.y-1)
            case 2:
                return (self.x+1, self.y)
            case 3:
                return (self.x, self.y+1)
    
    def turnpos(self) -> int:
        match self.direction:
            case 0:
                return 3
            case 1:
                return 0
            case 2:
                return 1
            case 3:
                return 2

    def turn(self) -> None:
        match self.direction:
            case 0:
                self.direction = 3
            case 1:
                self.direction = 0
            case 2:
                self.direction = 1
            case 3:
                self.direction = 2


class Solution:
    def __init__(self, path: str) -> None:
        self.area = open(path, 'r').readlines()
        self.visited = [[0 for _ in line] for line in self.area]
        self.past: set[tuple[int, int, int]] = set()
        for x, line in enumerate(self.area):
            for y, element in enumerate(line):
                match element:
                    case '>':
                        self.guard = Guard(x, y, 3)
                        break
                    case '<':
                        self.guard = Guard(x, y, 1)
                        break
                    case 'v':
                        self.guard = Guard(x, y, 2)
                        break
                    case '^':
                        self.guard = Guard(x, y, 0)
                        break   
        self.visits()

    def __repr__(self) -> str:
        out = ''
        for x, line in enumerate(self.visited):
            out += '|'
            for y, elm in enumerate(line):
                if elm == 0:
                    out += ' |'
                else:
                    out += str(self.visited[x][y])+'|'
            out += '\n'
        return out

    def cycle(self) -> None:
        self.past.add((self.guard.x, self.guard.y, self.guard.direction))

    def visits(self) -> None:
        self.visited[self.guard.x][self.guard.y] = 1

    def canMove(self, guard:Guard = None) -> bool:
        guard = self.guard if guard==None else guard

        match guard.direction:
            case 0:
                return guard.x - 1 >= 0
            case 1:
                return guard.y - 1 >= 0
            case 2:
                return guard.x + 1 < len(self.area)
            case 3:
                return guard.y + 1 < len(self.area[0])
    
    def moving(self): # partie 1
        self.cycle()
        while self.canMove():
            x, y = self.guard.movepos()
            if self.area[x][y] == '#':
                self.guard.turn()
            else:
                self.guard.move()
                self.visits()
                self.cycle()

        return self.visits

    @timer
    def partie1(self):
        self.moving()
        return self.points()
    
    @timer
    def partie2(self):
        cpt = 0
        for (x, y, dir) in self.past:
            g = Guard(x, y, dir)
            x0, y0 = g.movepos(g.direction)

            if not self.canMove(g) or self.area[x0][y0] == '#':
                continue

            tmp = set()
            while self.canMove(g):
                x, y = g.movepos(g.direction)

                if self.area[x][y] == '#' or (x == x0 and y == y0):
                    g.turn()
                else:
                    g.move()

                if (g.x, g.y, g.direction) in tmp:
                    cpt += 1
                    break
                else:
                    tmp.add((g.x, g.y, g.direction))
        return cpt

    def points(self):
        cpt = 0
        for line in self.visited:
            for elm in line:
                if elm != 0:
                    cpt += 1
        return cpt


if __name__ == "__main__":
    s = Solution("jour6.txt")
    assert s.partie1() == 4988
    assert s.partie2() == 1845
