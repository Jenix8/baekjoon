# while True : 
#     try : 
#         A, B =map(int, input().split())
#         print(A+B)
#     except : break

import sys
Ls = sys.stdin.readlines()
for L in Ls : print(sum(map(int, L.split())))