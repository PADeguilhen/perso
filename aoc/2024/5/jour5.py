class Solution:
    def __init__(self, path: str) -> None:
        self.order, self.pages = self.parse(path)
        
    def parse(self, path: str):
        inp = open(path, 'r').readlines()

        order = {}
        pages = []
        isPage = False
        for line in inp:
            if line == '\n':
                isPage = True
                continue
            if not isPage:
                ab = line.split('|')
                if int(ab[0]) in order.keys():
                    order[int(ab[0])].append(int(ab[1]))
                else:
                    order[int(ab[0])] = [int(ab[1])]
            else:
                pages.append([int(i) for i in line.split(',')])
        return order, pages

    def partie12(self):
        partie1 = 0
        partie2 = 0
        for line in self.pages:
            for i, page in enumerate(line):
                if not page in self.order.keys():
                    continue
                target = self.order[page]

                for j in line[:i+1]:
                    if j in target:
                        break
                else:
                    continue
                break
            else:
                partie1 += line[len(line)//2]
                continue
            nv = []
            queue = line

            while queue:
                choix = queue.pop(0)
                valide = True
                for elmt in queue:
                    if elmt in self.order.keys() and choix in self.order[elmt]:
                        valide = False
                        break
                if valide:
                    nv.append(choix)
                else:
                    queue.append(choix)

            partie2 += nv[len(nv)//2]
        return partie1, partie2

if __name__ == "__main__":
    s = Solution("jour5.txt")
    p1, p2 = s.partie12()
    print(f"{p1}\n{p2}")
    assert p1 == 5732
    assert p2 == 4716