from collections import Counter

class Solution:
    def __init__(self, path: str):
        self.inp = [['A' if i == 'A' else int(i) for i in line.strip()] for line in open(path, 'r').readlines()]
        self.numpad = {
            7: (0, 0),
            8: (0, 1),
            9: (0, 2),
            6: (1, 2),
            5: (1, 1),
            4: (1, 0),
            3: (2, 2),
            2: (2, 1),
            1: (2, 0),
            0: (3, 1),
            'A': (3, 2),
        }
        self.numpad.update({v:k for k, v in self.numpad.items()})
        self.keypad = {
            '^': (0, 1),
            'A': (0, 2),
            '<': (1, 0),
            'v': (1, 1),
            '>': (1, 2)
        }
        self.keypad.update({v:k for k,v in self.keypad.items()})

    def path(self, code: list[int | str] | str, pad: dict[str|int, int]):
        now = 'A'
        res = []
        for target in code:
            (ln, cn), (lt, ct) = pad[now], pad[target]
            ver = lt - ln
            hor = ct - cn

            verti = "v"*ver + "^"*-ver
            horiz = ">"*hor + "<"*-hor
            if hor > 0 and (lt, cn) in pad:
                res.append(verti + horiz + "A")
            elif (ln, ct) in pad:
                res.append(horiz + verti + "A")
            elif (lt, cn) in pad:
                res.append(verti + horiz + "A")
            now = target
        return Counter(res)

    def complexity(self, res: list[int]):
        cpt = 0
        for i, lenght in enumerate(res):
            cpt += lenght * sum(elm*10**j for j, elm in enumerate(self.inp[i][-2::-1]) if elm != 'A' )
        return cpt

    def iterateur(self, depth):
        total = [self.path(route, self.numpad) for route in self.inp]
        for _ in range(depth):
            new_routes = []
            for route_counter in total:
                new_route = Counter()
                for sub_route, nb in route_counter.items():
                    new_counts = self.path(sub_route, self.keypad)
                    for k in new_counts:
                        new_counts[k] *= nb
                    new_route.update(new_counts)
                new_routes.append(new_route)
            total = new_routes
        return self.complexity([sum(nb for nb in cpt.values()) for cpt in total])

    def partie1(self):
        return self.iterateur(3)

    def partie2(self):
        return self.iterateur(26)


if __name__ == "__main__":
    s = Solution("jour21.txt")
    p1 = s.partie1()
    print(p1)
    p2 = s.partie2()
    print(p2)
    assert p1 == 169390
    assert p2 == 210686850124870
