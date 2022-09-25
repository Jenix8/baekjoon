import sys

def IS_PRIME(i, prime) :
    Is_prime, k = 1, i ** 0.5
    for j in prime :
        if j <= k :
            if i % j == 0 :
                Is_prime = 0
                break
        else : break
    if Is_prime == 1 : return 1
    else : return 0

prime = [3]
for i in range(5, 1000, 2) :
    if IS_PRIME(i, prime) : prime.append(i)
prime = [2] + prime

M, N = map(int, sys.stdin.readline().rstrip().split())

if N <= 1000 :
    i = 0
    while prime[i] <= N :
        if prime[i] < M : 
            i += 1
            continue
        
        print(prime[i])
        i += 1
else :
    for i in range(M, N+1) :
        if i <= 1000 :
            if i in prime :
                print(i)
            continue
        if IS_PRIME(i, prime) : print(i)