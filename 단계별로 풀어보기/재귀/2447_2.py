Nine = ['*********', '* ** ** *', '***   ***', '* *   * *']
Order = [0, 1, 0, 2, 3, 2, 0, 1, 0]

def PrintStar(n, r, c) :
    if n == 9 :
        print(Nine[Order[r % 9]], end = '')
        return
    
    n = n // 3
    if (r // n) * (c // n) == 1 : print('         ', end = '')
    else : PrintStar(n, r % n, c % n)
    
N = int(input())
if N == 3 : print('***\n* *\n***')
else :
    for r in range(N) :
        for c in range(0, N, 9) :
            PrintStar(N, r, c)
        print("")