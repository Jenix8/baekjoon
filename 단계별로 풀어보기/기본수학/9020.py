prime = [3]

for i in range(5, 10000, 2) :
    SW = 0
    for j in prime :
        if i % j == 0 :
            SW = 1
            break
    if SW == 0 : prime.append(i)

T = int(input())
# Ex = []
# for i in range(4, 10000, 2) : Ex.append(i)
# T = len(Ex)
result = []

for t in range(T) :    
    n = int(input())
    # n = Ex[t]
    if n != 4 :
        if n % 4 == 2 : a, b = int(n/2), int(n/2)
        else : a, b = int((n/2) - 1), int((n/2) + 1)
            
        while (not a in prime) or (not b in prime) : a, b = a - 2, b + 2
    
    else : a, b = 2, 2
          
    L = [a, b]
    result.append(L)
    
for t in range(T) :
    print(result[t][0], result[t][1])