import sys
import sys

T1 = {}
T2 ={}
C = {}
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    T1[key] = T1.get(key,0) + int(value)
    cor = T1.get(key)
    cor2, cor3 = cor.strip().split(";")
    T2[key] = T2.get(key,0) + int(cor2)

    C[key] = C.get(key,0) + 1

for key in T2:
    av = int(T2.get(key,0)/C.get(key,0))
    avs = str(av)
    print(key + "\t" + avs)