T = int(input())
count = 0
for t in range(T) :
    S = input()
    SW, Alpha, Recent = 1, [False]*26, ''
    for i in range(len(S)) :
        if Alpha[ord(S[i])-97] == False :
            Recent = S[i]
            Alpha[ord(S[i])-97] = True
        elif Alpha[ord(S[i])-97] == True and Recent != S[i] :
            SW = 0
            break
    if SW == 1 : count += 1
print(count)

## 56B
print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)