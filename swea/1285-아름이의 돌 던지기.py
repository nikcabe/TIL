T = int(input())

for tc in range(1,1+T):
    n = int(input())
    arr = list(map(int,input().split()))
    num_lst = []
    cnt = 0
    min_v = 99999
    for i in range(n):
        if arr[i] > 0:
            num_lst.append(arr[i])
        elif arr[i] < 0:
            arr[i] *= -1
            num_lst.append(arr[i])
        else:
            num_lst.append(arr[i])
    for j in num_lst:
        if min_v > j:
            min_v = j
    for k in num_lst:
        if min_v == k:
            cnt += 1
    print(f'#{tc} {min_v} {cnt}')