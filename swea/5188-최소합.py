def f(i,j,sum_num):
    global min_num
    if i >= N or j >= N:
        return
    elif sum_num > min_num:
        return
    elif i == N-1 and j == N-1:
        sum_num += arr[i][j]
        if sum_num < min_num:
            min_num = sum_num
        return
    else:
        f(i, j+1, sum_num+arr[i][j])
        f(i+1, j, sum_num+arr[i][j])

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_num = N * 10 * 2
    f(0,0,0)
    print(f'#{tc} {min_num}')