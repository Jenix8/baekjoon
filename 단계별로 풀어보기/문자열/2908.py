A, B = map(list, input().split())
A.reverse()
B.reverse()
A, B = int(''.join(A)), int(''.join(B))
print(A) if A>B else print(B)