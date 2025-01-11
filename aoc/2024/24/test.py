import sys
import operator

L = sys.stdin.read().strip().split('\n\n')
rules = []
Zs = set()
for op in L[1].split('\n'):
    inp,out = op.split(' -> ')
    a,op,b = inp.split( )
    if op == 'AND': op = operator.and_
    if op == 'OR': op = operator.or_
    if op == 'XOR': op = operator.xor
    rules.append(((a, op, b), out))
    if out.startswith('z'):
        Zs.add(out)

G = dict()
for gate in L[0].split('\n'):
    gate,val = gate.split(': ')
    G[gate] = val == '1'

def Solve(Gates):
    Done = set()

    lend = len(Done)
    while any([o not in Done for o in Zs]):
        for ip, op in rules:
            if op in Done:
                continue
            a,bl,b = ip
            if a in Gates and b in Gates:
                ans = None
                ans = bl(Gates[a], Gates[b])
                assert ans != None
                Gates[op] = ans
                Done.add(op)
        if len(Done) == lend:
            return 0
        else:
            lend = len(Done)

    bits = sorted(Zs, reverse=True)
    ans = 0
    for b in bits:
        ans = ans << 1
        ans += Gates[b]
    return ans
print(Solve(G.copy()))

for r in rules:
    a, o, b = r[0]
    if a in ['x00', 'y00'] and b in ['x00', 'y00'] and o == operator.and_:
        carry = r[1]
        break

swaps = set()
def TestAdder(num, carry):
    x = f'x{num:02}'
    y = f'y{num:02}'
    z = f'z{num:02}'

    xor1 = None
    xor2 = None
    and1 = None
    and2 = None
    for r in rules:
        a, o, b = r[0]
        if o == operator.xor and x in [a,b] and y in [a,b]:
            xor1 = r[1]
        if o == operator.and_ and x in [a,b] and y in [a,b]:
            and1 = r[1]

    assert xor1 != None
    assert and1 != None
    if and1 == z:
        swaps.add(and1)

    for r in rules:
        a, o, b = r[0]
        if o == operator.xor and xor1 in [a,b] and carry in [a,b]:
            if r[1] != z:
                swaps.add(r[1])
                swaps.add(z)

        if o == operator.and_ and xor1 in [a,b] and carry in [a,b]:
            and2 = r[1]


    if and2 == None:
        swaps.add(and1)
        swaps.add(xor1)
        (and1, xor1) = (xor1, and1)
        for r in rules:
            a, o, b = r[0]
            if o == operator.xor and xor1 in [a,b] and carry in [a,b]:
                if r[1] != z:
                    swaps.add(r[1])
                    swaps.add(z)

            if o == operator.and_ and xor1 in [a,b] and carry in [a,b]:
                and2 = r[1]
    assert and2 != None, (xor1, carry)

    if and2 == z:
        swaps.add(and2)

    for r in rules:
        a, o, b = r[0]
        if o == operator.xor and xor1 in [a,b] and carry in [a,b]:
            xor2 = r[1]
            break
    assert xor2 != None
    if xor2 != z:
        swaps.add(z)
        swaps.add(r[1])
        if and1 == z:
            xor2 = z
            and1 = r[1]

    for r in rules:
        a, o, b = r[0]
        if o == operator.or_ and and1 in [a,b] and and2 in [a,b]:
            if r[1] == z:
                swaps.add(r[1])
                if xor2 in swaps:
                    return xor2
            return r[1]
        elif o == operator.or_ and and1 in [a,b] and xor2 in [a,b]:
            return r[1]
    assert False
for i in range(1,len(Zs)-1):
    carry = TestAdder(i, carry)
print(*sorted(swaps), sep=',')