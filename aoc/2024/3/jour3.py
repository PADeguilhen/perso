import re

class Solution:
    def __init__(self, path: str) -> None:
        self.input = open(path, 'r').read()
        
    def partie1(self):
        muls = re.findall(r"mul\(\d*,\d*\)", self.input)
        sum = 0
        for mul in muls:
            ab = re.findall(r"\d+", mul)
            sum += int(ab[0]) * int(ab[1])
        return sum
    
    def partie2(self):
        muls = re.findall(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", self.input)
        sum = 0
        counting = True
        for mul in muls:
            if mul == "do()":
                counting = True
                continue
            if mul == "don't()":
                counting = False
                continue

            if counting:
                ab = re.findall(r"\d+", mul)
                sum += int(ab[0]) * int(ab[1])
        return sum

if __name__ == "__main__":
    s = Solution("jour3.txt")
    print(s.partie1())
    print(s.partie2())
    assert s.partie1() == 187825547
    assert s.partie2() == 85508223
