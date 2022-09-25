def factorization(N, factor) :
    if N == 1 : return
    if N % 2 == 0 : 
        factor.append(2)
        factorization(int(N/2), factor)
        return
    for i in range(3, N+1, 2) :
        if N % i == 0 :
            factor.append(i)
            factorization(int(N/i), factor)
            break
        if N == i :
            factor.append(i)

N = int(input())      
if N != 1 :
    factor = []
    factorization(N, factor)
    if len(factor) == 0 : print(N)
    else : 
        for f in factor : print(f)