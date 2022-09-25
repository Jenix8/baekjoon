import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
20
strN = str(N)
l = len(strN)
for i in range(min(l * N, M)) :
    print(strN[i % l], end = '')