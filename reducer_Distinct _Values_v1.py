import sys

D = {}
for line in sys.stdin:
    list1 = line.strip().split("\t")
    D[list1[0]] = 1

for key, value in D.items():
    print(key)