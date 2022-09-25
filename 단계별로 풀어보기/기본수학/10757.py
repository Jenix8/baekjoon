A, B = map(list, input().split())
A.reverse()
B.reverse()
A, B = list(map(int, A)), list(map(int, B))
C = []
m, M, carry = min(len(A), len(B)), max(len(A), len(B)), 0
if len(A) >= len(B) : ALTB = True ## A is Longer Than or same to B 
else : ALTB = False
for i in range(M) :
    if i < m :
        C.append((carry + A[i] + B[i]) % 10)
        if carry + A[i] + B[i] >= 10 : carry = 1
        else : carry = 0
    else :
        if ALTB :
            C.append((carry + A[i]) % 10)
            if carry + A[i] >= 10 : carry = 1
            else : carry = 0
        else :
            C.append((carry + B[i]) % 10)
            if carry + B[i] >= 10 : carry = 1
            else : carry = 0
if carry == 1 : C.append(1)
C.reverse()
C = list(map(str, C))
print(int(''.join(C)))

# A, B = map(int, input().split())
# print(A + B)