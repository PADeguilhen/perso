import re

class Solution:
    def __init__(self, path) -> None:
        self.input = open(path, 'r').readlines()

    def partie1(self):
        sum = 0
        for line in self.input:
            sum += len(re.findall(r"XMAS", line))
            sum += len(re.findall(r"SAMX", line))

        for i, line in enumerate(self.input[:-3]):
            for j in range(len(line)-4):
                diag = self.input[i][j] + self.input[i+1][j+1] + self.input[i+2][j+2] + self.input[i+3][j+3]
                if diag == "XMAS" or diag == "SAMX":
                    sum += 1
            
            for j in range(3, len(line)):
                adiag = self.input[i][j] + self.input[i+1][j-1] + self.input[i+2][j-2] + self.input[i+3][j-3]
                if adiag == "XMAS" or adiag == "SAMX":
                    sum += 1
    
            for j in range(len(line)-1):
                colmn = self.input[i][j] + self.input[i+1][j] + self.input[i+2][j] + self.input[i+3][j]
                if colmn == "XMAS" or colmn == "SAMX":
                    sum += 1
        return sum

    def partie2(self):
        cpt = 0
        for i in range(1, len(self.input)-1):
            for j in range(1, len(self.input[0])-1):
                diag = self.input[i-1][j-1] + self.input[i][j] + self.input[i+1][j+1]
                adiag = self.input[i+1][j-1] + self.input[i][j] + self.input[i-1][j+1]
                if (diag == "MAS" or diag == "SAM") and (adiag == "MAS" or adiag == "SAM"):
                    cpt += 1
        return cpt

if __name__ == "__main__":
    s = Solution("jour4.txt")
    print(s.partie1())
    print(s.partie2())
    assert s.partie1() == 2462
    assert s.partie2() == 1877
