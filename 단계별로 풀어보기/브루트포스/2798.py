N, M = map(int, input().split())
Card_set = list(map(int, input().split()))

Current_sum = 0
for i in range(N) :
    for j in range(N) :
        if j > i :
            for k in range(N) :
                if k > i and k > j :
                    Sum = Card_set[i] + Card_set[j] + Card_set[k]
                    if Sum > Current_sum and Sum <= M : Current_sum = Sum

print(Current_sum)