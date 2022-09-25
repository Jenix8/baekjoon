## Mine
N = int(input())
i, count = 0, 0
while True :
    i += 1
    if '666' in str(i) : count += 1
    if count == N : 
        print(i)
        break
    
## 72ms
def check_num(check_number, jump_number):
    if check_number > jump_number:
        return 0, check_number-jump_number
    else:
        return 1, check_number


def jump_num(c, c_num):
    str_c = str(c)
    if str_c[-3:] == '666':
        j_num = 999
        flag, r_num = check_num(c_num, j_num)
    elif str_c[-2:] == '66':
        j_num = 99
        flag, r_num = check_num(c_num, j_num)
        if flag == 1:
            flag = 6
    elif str_c[-1] == '6':
        j_num = 9
        flag, r_num = check_num(c_num, j_num)
        if flag == 1:
            flag = 66
    else:
        return 0, c_num
    return flag, r_num


num = int(input())
count_num = num

if num == 1:
    print('666')
    quit()

for count in range(0, num):
    count_num -= 1

    if str(count).find('6') != -1:
        f, remain_num = jump_num(count, count_num)
        if f == 1:
            print(str(count) + "%03d" % remain_num)
            break
        elif f == 6:
            print(str(count) + str(f) + "%02d" % remain_num)
            break
        elif f == 66:
            print(str(count) + str(f) + str(remain_num))
            break
        else:
            count_num = remain_num
    if count_num == 0:
        print(str(count)+'666')
        break
