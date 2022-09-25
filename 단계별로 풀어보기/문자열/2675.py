T = int(input())
for t in range(T) :
    R, S = input().split()
    R = int(R)
    for r in range(len(S)) :
        print(R * S[r], end='')
    print("")