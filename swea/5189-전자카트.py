def f(i):
    global min_value
    global i_lst
    # 기저조건
    if i == n-1:
        sum_num = 0
        i_arr = [0]+i_lst+[0]
        for k in range(n):
            sum_num += arr[i_arr[k]][i_arr[k+1]]
        if min_value > sum_num:
            min_value = sum_num

    else:
        for j in range(i,n-1):
            i_lst[i],i_lst[j] = i_lst[j],i_lst[i]
            f(i+1)
            i_lst[i], i_lst[j] = i_lst[j], i_lst[i]

T = int(input())

for tc in range(1,1+T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    i_lst = [z for z in range(1,n)]
    min_value = 1001
    f(0)
    print(f'#{tc} {min_value}')