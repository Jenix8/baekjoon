## Maybe TimeOut

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

for i in range(10**(M-1), 10**M) :
    if i > (N + 1) * (10**(M-1)) : break

    count = 0
    for j in range(1, N+1) :
        if str(j) in str(i) : count += 1
    
    if count == M :
        for s in str(i) : print(s, end=' ') 
        print("")