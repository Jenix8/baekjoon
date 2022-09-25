N = int(input())

First = int(input())
m, M = First, First
numbers, count = [First], []

for _ in range(N-1) :
    Cur = int(input())
    if m > Cur : m = Cur
    if M < Cur : M = Cur
    numbers.append(Cur)

count = [0] * (M-m+1)

for i in range(N) : count[numbers[i] - m] += 1
for n in range(len(count)) :
    for _ in range(count[n]) : print(n+m)