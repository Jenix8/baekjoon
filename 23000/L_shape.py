def count_one(L, R, C, r, c, CS, RS) :
        East, South, West, North, a, b = 0, 0, 0, 0, 0, 0
        
        for Lst in CS :
            if Lst[0] <= c and Lst[0] + Lst[1] - 1 >= c :
                a = 1
                East = Lst[0] + Lst[1] - c
                West = c - Lst[0] + 1
                if West == Lst[1] : CS.remove(Lst)
                break 

        if a == 0 :
            for e in range(c, C) :
                if L[r][e] == 1 :
                    East += 1
                else : break
                            
            West = 1
            if East > 1 : CS.append([c, East])
            
        for Lst in RS[c] :
            if Lst[0] <= r and Lst[0] + Lst[1] - 1 >= r :
                b = 1
                South = Lst[0] + Lst[1] - r
                North = r - Lst[0] + 1
                if North == Lst[1] : RS[c].remove(Lst)
                break 
        
        if b == 0 :
            for s in range(r, R) :
                if L[s][c] == 1 :
                    South += 1
                else : break
                
            North = 1
            if South > 1 : RS[c].append([r, South])
            
        return East, South, West, North
    
def count_LShape(a, b) :
    if a == 1 or b == 1 : return 0
    else :
        count = 0 
        count += min(b, a // 2) - 1
        count += min(a, b // 2) - 1
        return count    
    
def count_total_LShape(A, B, C, D) :
    Count = 0
    Count += count_LShape(A, B)
    Count += count_LShape(B, C)
    Count += count_LShape(C, D)
    Count += count_LShape(D, A)
    return Count
    
T = int(input())
count = []

for t in range(0, T) :
    count.append(0)

    R, C = input().split()
    R, C = int(R), int(C)
    
    List, Row, CS, RS = [], [], [], []
    
    for l in range(0, R) :
        Row = list(input().split())
        Row = list(map(int, Row))
        List.append(Row)
        Row = []
    
    for p in range(0, C) : RS.append([])
        
    for i in range(0, R) :
        for j in range(0, C) :
            if List[i][j] == 1 :
                E, S, W, N = count_one(List, R, C, i, j, CS, RS)
                count[t] += count_total_LShape(E, S, W, N)
                
for t in range(0, T) :
    print("Case #%d: %d" % (t+1, count[t]))