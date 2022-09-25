import sys
N = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
M, count = max(numbers), 0

prime = [True] * (M+1)
prime[0], prime[1] = False, False
for i in range(2, M+1) :
    if prime[i] :
        for j in range(2*i, M+1, i) : prime[j] = False
        
for i in range(N) :
    if prime[numbers[i]] : count += 1
    
print(count)