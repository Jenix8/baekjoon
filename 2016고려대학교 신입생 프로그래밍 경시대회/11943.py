import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
C, D = map(int, sys.stdin.readline().rstrip().split())

print(min(A+D, B+C))