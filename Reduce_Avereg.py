import sys

T = {}
C = {}
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    T[key] = T.get(key,0) + int(value)
    C[key] = C.get(key,0) + 1

for key in T:
    av = int(T.get(key,0)/C.get(key,0))
    avs = str(av)
    print(key + "\t" + avs)