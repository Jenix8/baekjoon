## 160B
S = input()
Alpha = [-1]*26
for i in range(len(S)) :
    o = ord(S[i]) - 97
    if Alpha[o] == -1 : Alpha[o] = i
for i in range(26) : print(Alpha[i], end = ' ')

## 88B
S = input()
for i in range(97,123):
    A=S.find(str(chr(i)))
    print(A, end=' ')