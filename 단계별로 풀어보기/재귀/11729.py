def hanoi(n, a, b, c) :
    if n == 1 : 
        print(a, b)
        return 
    hanoi(n-1, a, c, b)
    print(a, b)
    hanoi(n-1, c, b, a)

N = int(input()) 
print(2 ** N - 1)
hanoi(N, 1, 3, 2)   