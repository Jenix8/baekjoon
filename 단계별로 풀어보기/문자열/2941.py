croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
count = len(S)
for a in croatia :
    count -= S.count(a)
count -= S.count('dz=') ## must subtracted by 2, but 1 already done by 'z='
print(count)