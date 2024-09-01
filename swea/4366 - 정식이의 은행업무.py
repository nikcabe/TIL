def binary(bin_num):
    result = 0
    for l in range(len(bin_num)):
        result += bin_num[l]*2**(len(bin_num)-l-1)
    return result

def tbin(tbin_num):
    result = 0
    if tbin_num[0] != 0:
        for l in range(len(tbin_num)):
            if tbin_num[l] == 1:
                result += 3 ** (len(tbin_num) - l-1)
            elif tbin_num[l] == 2 :
                result += 2 * 3 ** (len(tbin_num) - l-1)
    return result
T = int(input())

for tc in range(1,1+T):
    bin_num = list(map(int,input()))
    tbin_num = list(map(int,input()))
    bin_lst = []
    tbin_lst = []
    for i in range(1,len(bin_num)):
        if bin_num[i] == 1:
            bin_num[i] = 0
            bin_lst.append(binary(bin_num))
            bin_num[i] = 1
        else:
            bin_num[i] = 1
            bin_lst.append(binary(bin_num))
            bin_num[i] = 0
    for i in range(len(tbin_num)):
        if tbin_num[i] == 0:
            tbin_num[i] = 1
            tbin_lst.append(tbin(tbin_num))
            tbin_num[i] = 2
            tbin_lst.append(tbin(tbin_num))
            tbin_num[i] = 0
        elif tbin_num[i] == 1:
            tbin_num[i] = 0
            tbin_lst.append(tbin(tbin_num))
            tbin_num[i] = 2
            tbin_lst.append(tbin(tbin_num))
            tbin_num[i] = 1
        else:
            tbin_num[i] = 0
            tbin_lst.append(tbin(tbin_num))
            tbin_num[i] = 1
            tbin_lst.append(tbin(tbin_num))
            tbin_num[i] = 2
    print(bin_lst,tbin_lst)
    for j in range(len(bin_lst)):
        for k in range(len(tbin_lst)):
            if bin_lst[j] == tbin_lst[k]:
                print(f'#{tc} {bin_lst[j]}')