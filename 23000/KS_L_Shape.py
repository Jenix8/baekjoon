import sys

def count_Lshape(cell_count):
    count = 0
    left = cell_count['left']
    right = cell_count['right']
    up = cell_count['up']
    down = cell_count['down']

    # long left side
    count += max(0, min(left // 2 - 1, up - 1))
    count += max(0, min(left // 2 - 1, down - 1))
    # long right side
    count += max(0, min(right // 2 - 1, up - 1))
    count += max(0, min(right // 2 - 1, down - 1))
    # long upper side
    count += max(0, min(up // 2 - 1, left - 1))
    count += max(0, min(up // 2 - 1, right - 1))
    # long down side
    count += max(0, min(down // 2 - 1, left - 1))
    count += max(0, min(down // 2 - 1, right - 1))

    return count


T = int(sys.stdin.readline().rstrip())

for t in range(T):
    R, C = map(int, sys.stdin.readline().rstrip().split())

    grid = []
    for _ in range(R):
        grid.append(list(map(int, sys.stdin.readline().rstrip().split())))

    grid_count = []
    for _ in range(R):
        grid_count.append([{'left' : 0, 'right' : 0, 'up' : 0, 'down' : 0} for _ in range(C)])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                if c != 0:
                    grid_count[r][c]['left'] = grid_count[r][c - 1]['left'] + 1
                else:
                    grid_count[r][c]['left'] = 1
                
                if r != 0:
                    grid_count[r][c]['up'] = grid_count[r - 1][c]['up'] + 1
                else:
                    grid_count[r][c]['up'] = 1

    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if grid[r][c] == 1:
                if c != C - 1:
                    grid_count[r][c]['right'] = grid_count[r][c + 1]['right'] + 1
                else:
                    grid_count[r][c]['right'] = 1
                
                if r != R - 1:
                    grid_count[r][c]['down'] = grid_count[r + 1][c]['down'] + 1
                else:
                    grid_count[r][c]['down'] = 1

    count = 0
    
    for r in range(R):
        for c in range(C):
            count += count_Lshape(grid_count[r][c])

    print("Case #{}: {}".format(t + 1, count))
    