N = int(input())
negative, nonnegative = [], []

for _ in range(N) :
    Current = int(input())
    if Current >= 0 :
        for _ in range(len(nonnegative), Current+1) : nonnegative.append([])
        nonnegative[Current].append(Current)
    else :
        for _ in range(Current, -len(negative)) : negative.append([])
        negative[-Current-1].append(Current)

for _ in range(len(negative)) :
    for c in negative[-1] : print(c)
    negative.pop()
for i in range(len(nonnegative)) :
    for c in nonnegative[i] : print(c)