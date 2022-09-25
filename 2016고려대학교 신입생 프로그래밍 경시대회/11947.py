def F(n) :
    l = len(str(n))
    return 10 ** l - 1 - n

def G(n) :
    l = len(str(n))
    return int(10 ** l / 2)

T = int(input())
ans = []
maxi = 0

for i in range(T) :
    N = int(input())
    if(int(str(N)[0]) >= 5) :
        maxi = G(N) * (G(N) - 1)
    else :
        maxi = N * F(N)
    ans.append(maxi)
    
for i in range(T) :
    print(ans[i])