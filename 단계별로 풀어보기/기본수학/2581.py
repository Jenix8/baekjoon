M = int(input())
N = int(input())

prime = [True] * (N+1)
prime[0], prime[1] = False, False
for i in range(2, N+1):
    if prime[i] == True:
        for j in range(2 * i, N+1 ,i): prime[j] = False
        
count, m = 0, 0
for i in range(M, N+1) :
    if prime[i] == True :
        if count == 0 : m = i
        count += i

if count == 0 : print(-1)
else : print(count, m, sep='\n')