import time, sys

def Add_boxes(grid, R, C, M, ifl, count) :
    for r in range(R) :
        for c in range(C) :
            candidate = [grid[r][c]]
            for p in ifl :
                d = grid[p[0]][p[1]] - (abs(r - p[0]) + abs(c - p[1]))
                if d >= M - (R + C - 2) : 
                    candidate.append(d)
            m = max(candidate)
            count += m - grid[r][c]
            grid[r][c] = m       

    return count

T = int(input())
Case = []

for t in range(T) :    
    count, M, grid, ifl = 0, 0, [], []
    R, C = map(int, sys.stdin.readline().rstrip().split())
    
    for r in range(R) :
        # Row = list(map(int, sys.stdin.readline().rstrip().split()))
        Row = list(map(int, list(input().split())))
        grid.append(Row)
        if M < max(Row) : M = max(Row)
    
    start = time.time()
        
    for r in range(R) :    
        for c in range(C) : 
            if grid[r][c] >= M - (R + C - 2) : ifl.append((r, c))
    
    
    count = Add_boxes(grid, R, C, M, ifl, count)
    
    Case.append(count)
        
for t in range(0, T) :
    print("Case #%d: %d" % (t+1, Case[t]))
    
end = time.time()
print(end - start)