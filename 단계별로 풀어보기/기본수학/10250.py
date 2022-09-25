import math
T = int(input())
ACM = []
for t in range(T) :
    H, W, N = map(int, input().split())
    ACM.append(100 * (N % H) + math.ceil(N / H)) if N % H != 0 else ACM.append(100 * H + math.ceil(N / H))
for t in range(T) : print(ACM[t])
    
