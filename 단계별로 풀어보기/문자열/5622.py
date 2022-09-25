dial, sec, count = {}, 3, 0
for i in range(26) :
    if chr(i+65) in ['D', 'G', 'J', 'M', 'P', 'T', 'W'] : sec += 1
    dial[chr(i+65)] = sec
S = input()
for i in range(len(S)) : count += dial[S[i]]
print(count)