import sys
Total = int(input())
N = int(input())

Sum = 0
for _ in range(N) :
    price, num = map(int, sys.stdin.readline().rstrip().split())
    Sum += price * num
    
print("Yes") if Total == Sum else print("No")