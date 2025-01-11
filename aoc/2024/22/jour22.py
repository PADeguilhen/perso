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
        self.inp = [int(lines.strip()) for lines in open(path, 'r').readlines()]
    
    @timer
    def partie12(self):
        res = []
        Moad = {}
        for sec in self.inp:
            visited = set()
            for monkey, now in Secret(sec, 2000):
                if len(monkey) < 4:
                    continue
                if tuple(monkey) in visited:
                    continue
                visited.add(tuple(monkey))
                Moad[tuple(monkey)] = Moad.get(tuple(monkey), 0) + now % 10
            res.append(now)
        
        maxi = -1
        for value in Moad.values():
            # print(key, value, maxi)
            if value > maxi:
                maxi = value
        return sum(res), maxi


class Secret:
    def __init__(self, first: int, depth: int):
        self.now = first
        self.depth = depth
        self.prev = None
        self.monkey = []
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.depth == 0:
            raise StopIteration

        self.prev = self.now % 10

        self.now = ((self.now << 6) ^ self.now) % (1<<24)
        self.now = ((self.now >> 5) ^ self.now) % (1<<24)
        self.now = ((self.now << 11) ^ self.now) % (1<<24)

        self.depth -= 1
        self.monkey.append((self.now % 10) - self.prev)
        if len(self.monkey) >= 5:
            self.monkey.pop(0)
        return self.monkey, self.now


if __name__ == "__main__":
    s = Solution("jour22.txt")
    p12 = s.partie12()
    print(p12)
    assert p12 == (16039090236, 1808)
