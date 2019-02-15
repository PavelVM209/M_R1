import sys

H = {}
for token in ("a", "e", "t", "a", "e"):
    h = H.get(token)
    if h and h > 0:
        H[token] = int(h) + int(1)
    else: H[token] = int(1)
for x in H:
    print(x + "\t" + str(H[x]))

##






