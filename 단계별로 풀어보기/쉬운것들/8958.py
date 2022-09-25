T = int(input())
score = []

for t in range(T) :
    Result = input()
    j, s = 0, 0
    for i in range(len(Result)) :
        if Result[i] == "O" :
            j += 1
            s += j
        else : j = 0
    score.append(s)

for t in range(T) : print(score[t])