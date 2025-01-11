class Solution:
    def __init__(self, path: str):
        self.lines = open(path, 'r').readlines()
        self.lines = [line.split(':') for line in self.lines]
        self.targets = [int(line[0]) for line in self.lines]
        self.ints = [[int(i) for i in line[1].split(' ')[1:]] for line in self.lines]

    def vals(self, intList, target, index=-1):
        index %= len(intList)
        if index == 0:
            yield intList[index]
        else:
            for val in self.vals(intList, target, index-1):
                if val <= target:
                    yield val + intList[index]
                    yield val * intList[index]
    
    def partie1(self):
        sum = 0
        for i, t in enumerate(self.targets):
            for val in self.vals(self.ints[i], t):
                if val == t:
                    sum += t
                    break
        return sum

    def vals2(self, intList, target, index=-1):
        index %= len(intList)
        if index == 0:
            yield intList[index]
        else:
            for val in self.vals2(intList, target, index-1):
                if val <= target:
                    yield val + intList[index]
                    yield val * intList[index]
                    yield int(str(val) + str(intList[index]))

    def partie2(self):
        sum = 0
        for i, t in enumerate(self.targets):
            for val in self.vals2(self.ints[i], t):
                if val == t:
                    sum += t
                    break
        return sum

if __name__ == "__main__":
    s = Solution("jour7.txt")
    p1 = s.partie1()
    p2 = s.partie2()
    print(p1)
    print(p2)
    assert p1 == 2664460013123
    assert p2 == 426214131924213
