while True :
    tri = list(map(int, input().split()))
    if tri[0] == tri[1] == tri[2] == 0 : break
    tri.sort()
    print("right") if tri[2] ** 2 == tri[0] ** 2 + tri[1] ** 2 else print("wrong")