import sys

Primes = [True]*10000
Primes[0] = False

for i in range(2,int(10000**0.5)+1):
    if Primes[i] == True:
        for j in range(i+i,10000,i):
            Primes[j] = False

A = int(input())

def check_(n):
    for i in range(n//2,n,1):
        if Primes[n-i] and Primes[i]:
            return print(n-i, i)

for i in range(A):
    n = int(sys.stdin.readline())
    check_(n)