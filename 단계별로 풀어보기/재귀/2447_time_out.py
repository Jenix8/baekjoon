def PrintStar(n, r, c) :
    if n == 3 :
        print("*", end='') if r*c != 1 else print(" ", end='')
        return
    
    n = n / 3
    if (r // n) * (c // n) != 1:
        PrintStar(n, r % n, c % n)
    else : print(" ", end='')
    
N = int(input())

for r in range(N) :
    for c in range(N) :
        PrintStar(N, r, c)
    print("")