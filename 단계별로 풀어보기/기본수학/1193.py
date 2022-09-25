X = int(input())
i = 1
while (i * (i + 1)) / 2 < X:
    i += 1
N = ((i * (i + 1)) / 2) - X
print("%d/%d" % (i-N, N+1)) if i % 2 == 0 else print("%d/%d" % (N+1, i-N))