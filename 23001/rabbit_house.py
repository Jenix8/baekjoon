import time

def Add_boxes(G, H, R, C, M, GCT, count) :
    for point in H[M] :
        GCT += 1
        
        if point[0] != R - 1 : 
            if G[point[0] + 1][point[1]] < M - 1 :
                height[G[point[0] + 1][point[1]]].remove((point[0] + 1, point[1]))
                count += (M - 1) - G[point[0] + 1][point[1]]
                G[point[0] + 1][point[1]] = M - 1 
                height[M - 1].append((point[0] + 1, point[1]))
        
        if point[0] != 0 : 
            if G[point[0] - 1][point[1]] < M - 1 :
                height[G[point[0] - 1][point[1]]].remove((point[0] - 1, point[1]))
                count += (M - 1) - G[point[0] - 1][point[1]]
                G[point[0] - 1][point[1]] = M - 1 
                height[M - 1].append((point[0] - 1, point[1]))
                
        if point[1] != C - 1 : 
            if G[point[0]][point[1] + 1] < M - 1 :
                height[G[point[0]][point[1] + 1]].remove((point[0], point[1] + 1))
                count += (M - 1) - G[point[0]][point[1] + 1]
                G[point[0]][point[1] + 1] = M - 1 
                height[M - 1].append((point[0], point[1] + 1))
                
        if point[1] != 0 : 
            if G[point[0]][point[1] - 1] < M - 1 :
                height[G[point[0]][point[1] - 1]].remove((point[0], point[1] - 1))
                count += (M - 1) - G[point[0]][point[1] - 1]
                G[point[0]][point[1] - 1] = M - 1 
                height[M - 1].append((point[0], point[1] - 1))
                
    return H, M-1, GCT, count

T = int(input())
Case = []
start = time.time()

for t in range(T) :    
    Case.append(0)
    count, M, Grid_Count = 0, 0, 0
    R, C = input().split()
    R, C = int(R), int(C)
    grid, height = [], []
    height.append([])
    
    for r in range(0, R) :
        Row = []
        Row = list(input().split())
        Row = list(map(int, Row))
        grid.append(Row)
        if M < max(Row) : M = max(Row)
        for m in range(len(height) - 1, M) : height.append([])
        for c in range(0, C) : height[Row[c]].append((r, c))
        
    while True :
        height, M, Grid_Count, count = Add_boxes(grid, height, R, C, M, Grid_Count, count)
        if Grid_Count == R * C : break       
    
    Case[t] = count
        
for t in range(0, T) :
    print("Case #%d: %d" % (t+1, Case[t]))
    
end = time.time()
print(end-start)