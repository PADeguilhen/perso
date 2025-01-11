from itertools import combinations
import time

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__} executed in {(t2-t1) * 1000:.4f}ms")
        return res
    return wrapper

class Solution:
    def __init__(self, path: str):
        self.start, self.adj, self.nodes = self.parse(path)
    
    def parse(self, path: str):
        start: set[str] = set()
        adj: dict[str, set[str]] = {}
        nodes: set[str] = set()

        with open(path, 'r') as f:
            for line in f.readlines():
                a, b = line.strip().split('-')
                nodes.update((a, b))
                if a[0] == 't':
                    start.add(a)
                if b[0] == 't':
                    start.add(b)
                adj[a] = adj.get(a, set()).union([b])
                adj[b] = adj.get(b, set()).union([a])
        return start, adj, nodes

    @timer
    def partie1(self):
        interWithT = set()
        for source in self.start:
            for a, b in combinations(self.adj[source], 2):
                if a in self.adj[b]:
                    interWithT.add(tuple(sorted((a, b, source))))
        return len(interWithT)

    def solution(self, cliques):
        maxi, clique = -1, {}
        for c in cliques:
            if len(c)> maxi:
                clique = list(c)
                maxi = len(c)
        clique.sort()
        return ",".join(clique)

    @timer
    def partie2(self):
        cliques = []
        for node in self.nodes:
            clique = {node}
            toVisit = [node]

            while toVisit:
                now = toVisit.pop()
                for neighbor in self.adj[now]:
                    if clique <= self.adj[neighbor]:
                        toVisit.append(neighbor)
                        clique.add(neighbor)
            cliques.append(clique)
        
        return self.solution(cliques)

if __name__ == "__main__":
    s = Solution("jour23.txt")
    p1 = s.partie1()
    print(p1)
    p2 = s.partie2()
    print(p2)