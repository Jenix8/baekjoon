def era(n, prime) :
    prime = [True] * (n+1)
    prime[0], prime[1] = False, False
    for i in range(2, n+1) :
        if prime[i] == True :
            for j in range(2*i, n+1, i) : prime[j] = False
    return prime
            
Case, Res, prime = [], [], []
while True :
    N = int(input())
    if N == 0 : break
    Case.append(N)
    
M = max(Case)
prime = era(2*M, prime)
for n in Case :
    count = 0
    for i in range(n+1, 2*n+1) :
        if prime[i] : count += 1
    Res.append(count)
for t in range(len(Res)) : print(Res[t])