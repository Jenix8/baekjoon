## Memory Exceed

# N = int(input())
# numbers, count = [], []
# M = 0
# for i in range(N) : 
#     tmp = int(input())
#     numbers.append(tmp)
#     if M < tmp : M = tmp
    
# for j in range(M) :
#     tmp = []
#     if j+1 in numbers :
#         for _ in range(numbers.count(j+1)) :
#             tmp.append(j+1)
#     count.append(tmp)
    
# for k in range(M) :
#     for a in count[k] :
#         print(a)
        
## Second trial

N = int(input())
count = [0]
for i in range(1, N+1) : 
    tmp = int(input())
    
    for _ in range(len(count), tmp + 1) :
        count.append(0)
    
    count[tmp] += 1
    
for j in range(1, len(count)) :
    if count[j] != 0 :
        for _ in range(count[j]) :
            print(j)