import heapq

class Solution:
    def __init__(self, path:str):
        self.inp: str = open(path, 'r').readline()
        self.computer, self.free_space = self.parse()
    
    def parse(self):
        computer: list[int | str] = []
        free_space: list[list[int]] = [[] for _ in range(10)]
        for i, elm in enumerate(self.inp):
            if i % 2 == 1: 
                if int(elm) > 0:
                    heapq.heappush(free_space[int(elm)], len(computer))
                    computer += ['.'] * int(elm)
            else:
                computer += [i//2]*int(elm)
        return computer, free_space

    def points(self, computer):
        ret = 0
        for i, elm in enumerate(computer):
            if elm == '.':
                continue
            ret += i * elm
        return ret

    def partie1(self):
        computer = self.computer.copy()
        right: int = len(computer) - 1
        sum: int = 0
        for index, elm in enumerate(computer):
            if index > right:
                right = index
                break
            if elm == '.':
                sum += computer[right]*index
                right -= 1
                while computer[right] == '.':
                    right -= 1
            else:
                sum += index * elm
        return sum

    def partie2(self):
        computer = self.computer.copy()
        index = len(computer)-1
        while index >= 0:
            if computer[index] == '.':
                index -= 1
                continue

            id = computer[index]
            width = 0
            while index >= 0 and computer[index] == id:
                index -= 1
                width += 1

            min = float('inf')
            best = -1
            for i, free in enumerate(self.free_space[width:]):
                if free != [] and min > free[0]:
                    min = free[0]
                    best = i + width
            if min == float("inf") or min > index:
                continue
            
            heapq.heappop(self.free_space[best])
            for i in range(width):
                computer[min + i] = id
                computer[index + 1 + i] = '.'
            heapq.heappush(self.free_space[best - width], min + width)

        return self.points(computer)

if __name__ == "__main__":
    s = Solution("jour9.txt")
    p1 = s.partie1()
    p2 = s.partie2()
    print(p1)
    print(p2)
    assert p1 == 6463499258318
    assert p2 == 6493634986625
