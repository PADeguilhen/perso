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
        self.locks, self.keys = self.parse(path)
    
    def parse(self, path):
        locks = []
        keys = []
        with open(path, 'r') as f:
            obj = [0]*5
            isLock = False
            for line in f.readlines():
                if line == '\n':
                    if isLock:
                        locks.append(obj)
                    else:
                        keys.append(obj)
                    obj, isLock = [0]*5, False
                    continue
                if line == ".....\n" and obj == [0]*5:
                    isLock = True
                    continue
                for i in range(len(obj)):
                    if line[i] == '#':
                        obj[i] += 1
        return locks, keys

    def canPut(self, l:int, k: int):
        for j, elm in enumerate(self.locks[l]):
            if self.keys[k][j] + elm > 7:
                return False
        return True
    
    #@timer
    def partie12(self):
        cpt = 0
        for k in range(len(self.keys)):
            for l in range(len(self.locks)):
                if self.canPut(l, k): cpt += 1
        return cpt


if __name__ == "__main__":
    s = Solution("jour25.txt")
    p1 = s.partie12()
    print(p1)
    assert p1 == 3395
