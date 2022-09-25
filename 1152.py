# S = input().strip()
# count = 1
# for i in range(len(S)) : 
#     if S[i] == ' ' : count += 1
# print(count)

import sys
print(len(list(sys.stdin.readline().strip().split())))