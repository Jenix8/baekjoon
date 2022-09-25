N = int(input())
fact, M = [], N
while M != 1 :
    if M % 2 == 0 : 
        M = M // 2
        fact.append(2)
        continue
    for i in range(3, M+1, 2) :
        if M % i == 0 : 
            M = M // i
            fact.append(i)
            break
if N != 1 :
    for f in fact : print(f)