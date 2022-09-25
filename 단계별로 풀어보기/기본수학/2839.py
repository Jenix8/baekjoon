# N = int(input())
# L = [0, 5, 10]
# R = -1

# for i in L :
#     if N >= i :
#         M = 5 * ((N - i) // 5)
#         if (N - M) % 3 == 0 : R = (M // 5) + ((N - M) // 3)
        
# print(R)

N = int(input())
L, X = [1, 2, 0, 1, -1], [1, 2, 4, 7]
R = (((N - 1) // 5) - L[(N % 5) - 1]) + (((N % 5) * 2) % 5)
if N in X : R = -1
print(R)