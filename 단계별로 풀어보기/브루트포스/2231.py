N = input()
digit = len(N)
N = int(N)

for i in range(max(N - 9 * digit, 1), N + 1) :
    if i == N : 
        print(0)
        break
    
    s, sum = str(i), i
    for j in range(len(s)) :
        sum += int(s[j])
    if sum == N :
        print(i)
        break    