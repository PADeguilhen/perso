class Solution:
    def __init__(self, path: str):
        self.values, self.operation = self.parse(path)

    def parse(self, path):
        with open(path, 'r') as f:
            values = {}
            operation = {}
            passedValues = False
            for line in f.readlines():
                if line == '\n':
                    passedValues = True
                    continue
                if not passedValues:
                    address, val = line.strip().split(': ')
                    values[address] = bool(int(val))
                else:
                    logic, result = line.strip().split(" -> ")
                    a, ope, b = logic.split(' ')
                    operation[result] = (ope, a, b)
        return values, operation
    
    def number(self, letter: chr, values):
        cpt = 0
        index = 0
        while True:
            try:
                cpt += values[f"{letter}{index:02}"] << index
                #print(f"{letter}{index:02}",values[f"{letter}{index:02}"])
                index += 1
            except:
                break
        return cpt

    def partie1(self):
        operation = self.operation.copy()
        values = self.values.copy()
        while operation:
            done = set()
            for val, (ope, a, b) in operation.items():
                if (a in values) and (b in values):
                    if ope == 'AND': 
                        values[val] = values[a] & values[b]
                    if ope == 'OR': 
                        values[val] = values[a] | values[b]
                    if ope == 'XOR': 
                        values[val] = values[a] ^ values[b]
                    done.add(val)
            for val in done:
                del operation[val]
        return self.number('z', values)

if __name__ == "__main__":
    s = Solution("jour24.txt")
    p1 = s.partie1()
    print(p1)
    assert p1 == 57344080719736
    