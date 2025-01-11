from enum import Enum

class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class Robot:
    def __init__(self, line: int, col:int):
        self.line = line
        self.col = col

    def move(self, direction: Direction) -> None:
        match direction:
            case Direction.UP:
                self.line = self.line - 1
            case Direction.LEFT:
                self.col = self.col - 1
            case Direction.DOWN:
                self.line = self.line + 1
            case Direction.RIGHT:
                self.col = self.col + 1
    
    def givePos(self) -> tuple[int, int]:
        return self.line, self.col


class Solution:
    def __init__(self, path: str):
        self.grid, self.grid2, self.instr = self.parse(path)
        l, c = self.robotpos()
        self.robot = Robot(l, c)
        self.robot2 = Robot(l, c*2)

    def __repr__(self):
        out = ""
        for line in self.grid:
            for elm in line:
                out+=elm
            out+='\n'
        for line in self.grid2:
            for elm in line:
                out+=elm
            out+='\n'
        return out

    def robotpos(self) -> tuple[int, int]:
        for l, line in enumerate(self.grid):
            for c, elm in enumerate(line):
                if elm =='@':
                    self.grid[l][c] = '.'
                    return l, c
        raise Exception("Where is the Robot?")

    def parse(self, path: str) -> tuple[list[list[str]], str]:
        grid = []
        grid2 = []
        instrSet = ""
        isGrid = True
        for line in open(path, 'r').readlines():
            if line == '\n':
                isGrid = False
                continue
            if isGrid:
                grid.append(list(line.strip()))
                grid2.append([])
                for i in line.strip():
                    if i == '@':
                        grid2[-1].append('.')
                        grid2[-1].append('.')
                    elif i == 'O':
                        grid2[-1].append('[')
                        grid2[-1].append(']')
                    else:
                        grid2[-1].append(i)
                        grid2[-1].append(i)
            else:
                instrSet += line.strip()
        return grid, grid2, instrSet

    def Handler(self, dir: Direction) -> None:
        self.robot.move(dir)
        l, c = self.robot.givePos()
        match dir:
            case Direction.UP:
                if not self.moveO(l, c, dir):
                    self.robot.move(Direction.DOWN)
                elif self.grid[l][c] == '.':
                    return
                return
            case Direction.LEFT:
                if not self.moveO(l, c, dir):
                    self.robot.move(Direction.RIGHT)
                elif self.grid[l][c] == '.':
                    return
                return
            case Direction.DOWN:
                if not self.moveO(l, c, dir):
                    self.robot.move(Direction.UP)
                elif self.grid[l][c] == '.':
                    return
                return
            case Direction.RIGHT:
                if not self.moveO(l, c, dir):
                    self.robot.move(Direction.LEFT)
                elif self.grid[l][c] == '.':
                    return
                return

    def moveO(self, line: int, col: int, dir: Direction):
        l0 = line
        c0 = col
        match dir:
            case Direction.UP:
                while self.grid[line][col] == 'O':
                    line -= 1
                if self.grid[line][col] == '#':
                    return False
                else:
                    self.grid[l0][c0], self.grid[line][col] = self.grid[line][col], self.grid[l0][c0]
            case Direction.LEFT:
                while self.grid[line][col] == 'O':
                    col -= 1
                if self.grid[line][col] == '#':
                    return False
                else:
                    self.grid[l0][c0], self.grid[line][col] = self.grid[line][col], self.grid[l0][c0]
            case Direction.DOWN:
                while self.grid[line][col] == 'O':
                    line += 1
                if self.grid[line][col] == '#':
                    return False
                else:
                    self.grid[l0][c0], self.grid[line][col] = self.grid[line][col], self.grid[l0][c0]
            case Direction.RIGHT:
                while self.grid[line][col] == 'O':
                    col += 1
                if self.grid[line][col] == '#':
                    return False
                else:
                    self.grid[l0][c0], self.grid[line][col] = self.grid[line][col], self.grid[l0][c0]
        return True

    def mvmt(self):
        for instr in self.instr:
            match instr:
                case '^':
                    self.Handler(Direction.UP)
                    self.Handler2(Direction.UP)
                case '<':
                    self.Handler(Direction.LEFT)
                    self.Handler2(Direction.LEFT)
                case 'v':
                    self.Handler(Direction.DOWN)
                    self.Handler2(Direction.DOWN)
                case '>':
                    self.Handler(Direction.RIGHT)
                    self.Handler2(Direction.RIGHT)

    def gps(self):
        cpt1, cpt2 = 0, 0
        for l, line in enumerate(self.grid):
            for c, col in enumerate(line):
                if col == 'O':
                    cpt1 += 100 * l + c
        for l, line in enumerate(self.grid2):
            for c, col in enumerate(line):
                if col == '[':
                    cpt2 += 100 * l + c
        return cpt1, cpt2
    
    def canPush(self, l: int, c:int, dir: Direction): # part II only for
        if dir == Direction.UP:
            ori = -1
        else:
            ori = 1

        if self.grid2[l][c] == '[':
            return self.canPush(l+ori, c, dir) and self.canPush(l+ori, c+1, dir)
        elif self.grid2[l][c] == ']':
            return self.canPush(l+ori, c-1, dir) and self.canPush(l+ori, c, dir)
        elif self.grid2[l][c] == '.':
            return True
        else:
            return False
    
    def moveRec(self, l, c, dir):
        if dir == Direction.UP:
            ori = -1
        else:
            ori = 1

        if self.grid2[l][c] == '[':
            if not self.grid2[l+ori][c] == '.':
                self.moveRec(l+ori, c, dir)
            self.grid2[l+ori][c], self.grid2[l][c] = self.grid2[l][c], self.grid2[l+ori][c]

            if not self.grid2[l+ori][c+1] == '.':
                self.moveRec(l+ori, c+1, dir)
            self.grid2[l+ori][c+1], self.grid2[l][c+1] = self.grid2[l][c+1], self.grid2[l+ori][c+1]

        elif self.grid2[l][c] == ']':
            if not self.grid2[l+ori][c] == '.':
                self.moveRec(l+ori, c, dir)
            self.grid2[l+ori][c], self.grid2[l][c] = self.grid2[l][c], self.grid2[l+ori][c]

            if not self.grid2[l+ori][c-1] == '.':
                self.moveRec(l+ori, c-1, dir)
            self.grid2[l+ori][c-1], self.grid2[l][c-1] = self.grid2[l][c-1], self.grid2[l+ori][c-1]


    def Handler2(self, dir: Direction):
        self.robot2.move(dir)
        l, c = self.robot2.givePos()
        if self.grid2[l][c] == '.':
            return
        c0 = c
        match dir:
            case Direction.UP:
                if not self.canPush(l, c, dir):
                    self.robot2.move(Direction.DOWN)
                else:
                    self.moveRec(l, c, dir)

            case Direction.LEFT:
                while self.grid2[l][c] in '[]':
                    c -= 1
                if self.grid2[l][c] == '#':
                    self.robot2.move(Direction.RIGHT)
                else:
                    self.grid2[l][c0] = '.'
                    for i in range(c0 - c):
                        if i % 2 == 0:
                            self.grid2[l][c+i] = '['
                        else:
                            self.grid2[l][c+i] = ']'

            case Direction.DOWN:
                if not self.canPush(l, c, dir):
                    self.robot2.move(Direction.UP)
                else:
                    self.moveRec(l, c, dir)

            case Direction.RIGHT:
                while self.grid2[l][c] in '[]':
                    c += 1
                if self.grid2[l][c] == '#':
                    self.robot2.move(Direction.LEFT)
                else:
                    self.grid2[l][c0] = '.'
                    for i in range(c - c0):
                        if i % 2 == 1:
                            self.grid2[l][c-i] = '['
                        else:
                            self.grid2[l][c-i] = ']'

    def partie12(self):
        self.mvmt()
        return self.gps()

if __name__ == "__main__":
    g = Solution("jour15.txt")
    p1, p2 = g.partie12()
    print(g)
    print(p1, p2)
    assert p1 == 1406392
    assert p2 == 1429013
