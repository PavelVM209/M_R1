import sys
D = {}
for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    (a, b) = (v, k)
    if D[a] and D[a] == k:
         z = 0
    else:    D[a] = D.get(a,0) + 1
for a, b in D.items():
    print(str(a) + "\t" + str(b))

# (lastKey, sum)=(None, 0)
#
# for line in sys.stdin:
#     (key, value) = line.strip().split("\t")
#     if lastKey and lastKey != key:
#         print (lastKey + '\t' + str(sum))
#         (lastKey, sum) = (key, int(value))
#     else:
#         (lastKey, sum) = (key, sum + int(value))
# if lastKey:
#     print (lastKey + '\t' + str(sum))