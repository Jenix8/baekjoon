import sys
x1, y1 = map(int, sys.stdin.readline().rstrip().split())
x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x3, y3 = map(int, sys.stdin.readline().rstrip().split())

d = (y1 - y2) * (x3 - x2) + (x2 - x1) * (y3 - y2)

if(d > 0) : print("1")
elif (d < 0) : print("-1")
else : print("0")
