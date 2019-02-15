
import sys


for line in sys.stdin:
    D = {}
    list1 = line.strip().split(",")
    D[list1[1]] = "1"

    for key, value in D.items():
        print(key + "\t" + value)