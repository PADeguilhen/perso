class Solution:
    def __init__(self, path: str):
        self.A, self.Program = self.parse(path)
        self.target = self.Program[::-1]

    def parse(self, path: str):
        lines = open(path, 'r').readlines()
        A = int(lines[0].split(' ')[-1])
        pro = [int(i) for i in lines[-1][9:].split(',')]
        return A, pro

    def computer(self, instr: list[int], a: int):
        ip, b, c = 0, 0, 0
        def combo(lit):
            if 0 <= instr[lit] <= 3:
                return instr[lit]
            elif instr[lit] == 4:
                return a
            elif instr[lit] == 5:
                return b
            elif instr[lit] == 6:
                return c
            else:
                raise Exception("Invalid Program")

        out = ""
        while ip < len(instr):
            op = instr[ip]
            match op:
                case 0: # adv
                    a >>= combo(ip+1)
                case 1: # bxl
                    b ^= instr[ip+1]
                case 2: # bst
                    b = combo(ip+1) % 8
                case 3: # jnz
                    if a != 0:
                        ip = instr[ip+1]
                        continue
                case 4: # bxc
                    b ^= c
                case 5: # out
                    out += str(combo(ip+1) % 8) + ','
                case 6: # bdv
                    b = a >> combo(ip+1)
                case 7: # cdv
                    c = a >> combo(ip+1)
            ip += 2
        return [int(i) for i in out.split(',')[:-1]]

    def partie1(self):
        return self.computer(self.Program, self.A)

    def partie2(self, depth: int = 0, a: int = 0):
        if depth == len(self.Program):
            return a
        else:
            for tmp in range(8):
                h = self.computer(self.Program, (a << 3) + tmp)
                if h and h[0] == self.target[depth]:
                    if res := self.partie2(depth = depth+1, a = (a << 3) + tmp):
                        return res


if __name__ == "__main__":
    s = Solution("jour17.txt")
    p1 = s.partie1()
    p2 = s.partie2()
    print(p1)
    print(p2)
    assert p1 == [7, 1, 3, 4, 1, 2, 6, 7, 1]
    assert p2 == 109019476330651
