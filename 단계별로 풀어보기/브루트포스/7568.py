T = int(input())
L = []
for t in range(T) : L.append(list(map(int, input().split())))
for i in range(T) :
    w, h = L[i][0], L[i][1]
    rank = 1
    for j in range(T) :
        if w < L[j][0] and h < L[j][1] : rank += 1
    L[i].append(rank)
for t in range(T) : print(L[t][2], end = ' ')
         