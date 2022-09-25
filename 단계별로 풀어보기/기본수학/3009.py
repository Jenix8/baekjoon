def another(a, b, c) :
    if a == b : return c
    elif b == c : return a
    else : return b

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(another(x1, x2, x3), another(y1, y2, y3))