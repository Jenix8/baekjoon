A, B = map(int, input().split())
C = int(input())
q, r = (B + C) // 60, (B + C) % 60
h = (A + q) % 24
print(h, r)