#!/c/Users/pmurzakov/Programs/Python27/


import sys

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token: print (token + "/t1")

