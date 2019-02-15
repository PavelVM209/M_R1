import sys

H = {}

for token in ("a", "e", "t", "a", "e"):
    H[token] = H.get(token,0) + 1

for x in H:
    print(x + "\t\t" + str(H[x]))


# for line in sys.stdin:
#     H = {}
#     for token in line.strip().split(" "):
#         h = H.get(token)
#         if h and h > 0:
#             H[token] = int(h) + int(1)
#         else: H[token] = int(1)
#     for x in H:
#         print(x + "\t" + str(H[x]))


# for line in sys.stdin:
#     for token in line.strip().split(" "):
#         if token:
#             sum = sum +1
#             H[token] = sum
#     for x in H:
#         print (dict.items(x))