import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
fish_bread = []


for i in range(N) :
    fish_bread.append(input())
    
for i in range(N) :
    for j in range(M - 1, -1, -1) :
        print(fish_bread[i][j], end='')
    print("")