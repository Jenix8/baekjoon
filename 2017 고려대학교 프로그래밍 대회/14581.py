name = input()
fan = ":fan:"

for i in range(9) :
    if (i == 4) : print(":" + name + ":", end='')
    else : print(fan, end='')
    
    if((i+1) % 3 == 0) : print("")