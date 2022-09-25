import sys, math

def Move(cell, N) :
    if N != 0 :
        tmp = cell[N]
        cell[N] = cell[0]
        cell[0] = tmp
    
def Add_boxes(grid, cell, statement, R, C, count) :
    N = 0
    while True :
        if cell[0][0] == -1 : break
        Current_cell = cell[0]
        h, x, y = Current_cell[0], Current_cell[1][0], Current_cell[1][1]
        if N == 0 :
            i = 1
            while cell[i][0] == cell[0][0] : i += 1
            N = i
        if statement[x][y] == 2 : 
            del cell[0]
            N -= 1
            continue
        
        del cell[0]
        N -= 1
        
        W, X, Y, Z = [x, x, y, y], [x-1, x+1, x, x], [y, y, y-1, y+1], [0, R-1, 0, C-1]
        
        for j in range(4) :
            if W[j] != Z[j] : 
                if statement[X[j]][Y[j]] == 0 :
                    if grid[X[j]][Y[j]] < h - 1 :
                        count += h - 1 - grid[X[j]][Y[j]]
                        grid[X[j]][Y[j]] = h - 1
                        statement[X[j]][Y[j]] = 1
                        cell = [(h-1, (X[j], Y[j]))] + cell
                        Move(cell, N)
        
        statement[x][y] = 2
    return count

def ifl_add(grid, R, C, M, ifl, count) :
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
    count, grid, cell, statement, M, ifl = 0, [], [], [], 0, []
    R, C = map(int, sys.stdin.readline().rstrip().split())
    
    for r in range(R) :
        Row = list(map(int, sys.stdin.readline().rstrip().split()))
        # Row = list(map(int, list(input().split())))
        grid.append(Row)
        if M < max(Row) : M = max(Row)
        S_Row = []
        for c in range(C) : S_Row.append(0)
        statement.append(S_Row)
        ## statement 0 : not yet checked
        ## statement 1 : not yet checked but changed by adjacent cell
        ## statement 2 : checked
        for c in range(C) : cell.append((Row[c], (r, c)))
    
    if cell[min(int(math.log2(R*C)), 10)][0] < M - (R + C - 2) :
        for r in range(R) :
            for c in range(C) :
                if grid[r][c] >= M - (R + C - 2) : ifl.append((r, c))        
        count = ifl_add(grid, R, C, M, ifl, count)    
    
    else :
        cell.sort(reverse=True)
        cell.append((-1, (-1, -1)))
        count = Add_boxes(grid, cell, statement, R, C, count)   

    Case.append(count)
    
for t in range(0, T) :
    print("Case #%d: %d" % (t+1, Case[t]))