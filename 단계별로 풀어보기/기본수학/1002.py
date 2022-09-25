T = int(input())
count = []
for t in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d == 0 :
        if r1 == r2 :
            count.append(-1)
        else :
            count.append(0)
        continue
    L = [r1, r2, d]
    L.sort()
    if L[2] < L[0] + L[1] : count.append(2)
    elif L[2] == L[0] + L[1] : count.append(1)
    else : count.append(0)
for t in range(T) : print(count[t])