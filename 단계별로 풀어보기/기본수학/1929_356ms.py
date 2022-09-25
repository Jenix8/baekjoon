m, n = map(int, input().split())

judge = [True] * (n+1)
judge[1] = False
t = int((n+1) ** 0.5)
for i in range(2, t+1):
    if judge[i] == True:
        for j in range(i+i, n+1, i):
            judge[j] = False

for k in range(m, n+1):
    if judge[k] == True:
        print(k)