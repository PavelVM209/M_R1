import sys

for line in sys.stdin:
    list = line.strip().split("\t")
    if list[1] == "user10":
        print(line, end="")