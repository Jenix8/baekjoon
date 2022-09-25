import sys
score1 = list(map(int, sys.stdin.readline().rstrip().split()))
score2 = list(map(int, sys.stdin.readline().rstrip().split()))

total1, total2 = 0, 0

for i in range(9) :
    total1 += score1[i]
    if(total1 > total2) : 
        print("Yes")
        break
    total2 += score2[i]
    if(total1 > total2) : 
        print("Yes")
        break
else : print("No")