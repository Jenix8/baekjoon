L, R = [], []
for k in range(14) :
    for i in range(0, 15) :
        floor = [0]
        for j in range(1, 15) :
            if i == 0 : floor.append(j)
            else : floor.append(floor[j-1]+L[i-1][j])
        L.append(floor)
    
T = int(input())
for t in range(T) :
    k = int(input())
    n = int(input())
    R.append(L[k][n])
for t in range(T) : print(R[t])