import sys
R, C = map(int, sys.stdin.readline().rstrip().split())
grid = []
for _ in range(R):
    grid.append(list(sys.stdin.readline().rstrip()))

m = 32    
for r in range(R-7) :
    for c in range(C-7) :
        ## FirstPoint = (r, c)
        Fr, Fc = r, c
        count1, count2 = 0, 0
        while True :
            if (Fr + Fc) % 2 == 0 : 
                if grid[Fr][Fc] != 'B' : count1 += 1
                else : count2 += 1
            else :
                if grid[Fr][Fc] != 'W' : count1 += 1
                else : count2 += 1
                
            # print(count1, count2)
            if (Fr - r == 7) and (Fc - c == 7) : break
            
            if Fc - c != 7 : Fc += 1
            else :
                Fc = c
                Fr += 1
        
        if m > min(count1, count2) : m = min(count1, count2)

print(m)