class Solution:
    def __init__(self, path: str):
        self.inp = [[int(elm) for elm in line[:-1]] for line in open(path, 'r').readlines()]

    def partie12(self):
        cpt1 = 0
        cpt2 = 0
        for l, line in enumerate(self.inp):
            for c, elm in enumerate(line):
                if elm == 0:
                    c1, c2 = self.parcours(l, c)
                    cpt1 += c1
                    cpt2 += c2
        return cpt1, cpt2

    def parcours(self, l0: int, c0: int) -> int:
        nines: set[tuple[int, int]] = set()
        cpt1, cpt2 = 0, 0
        parcours: list[tuple[int, int]] = [(l0, c0)]
        while len(parcours) != 0:
            l, c = parcours.pop()
            if self.inp[l][c] == 9:
                if not (l, c) in nines:
                    cpt1 += 1
                nines.add((l, c))
                cpt2 += 1

            if l != 0 and self.inp[l-1][c] == self.inp[l][c] + 1:
                parcours.append((l-1, c))
            if c != 0 and self.inp[l][c-1] == self.inp[l][c] + 1:
                parcours.append((l, c-1))
            if l < len(self.inp) - 1 and self.inp[l+1][c] == self.inp[l][c] + 1:
                parcours.append((l+1, c)) 
            if c < len(self.inp[0]) - 1 and self.inp[l][c+1] == self.inp[l][c] + 1:
                parcours.append((l, c+1))
        return cpt1, cpt2

if __name__ == "__main__":
    s = Solution("jour10.txt")
    p1, p2 = s.partie12()
    print(p1, p2)
    assert p1, p2 == (733, 1514)