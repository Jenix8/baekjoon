# S = input().upper()
# F, Out = [0] * 26, []
# for i in range(len(S)) : F[ord(S[i])-65] += 1
# M = max(F)
# for j in range(26) : 
#     if F[j] == M : Out.append(j)
# print(chr(Out[0]+65)) if len(Out) == 1 else print("?")

S = input().upper()
SL, count = list(set(S)), []
for i in SL : count.append(S.count(i))
print(SL[count.index(max(count))]) if count.count(max(count)) == 1 else print("?")