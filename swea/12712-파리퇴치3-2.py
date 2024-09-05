T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    dk = [1,1,-1,-1]
    dl = [1,-1,-1,1]
    result = 0
    for i in range(N):
        for j in range(N):
            sum_num = 0
            sum_num = arr[i][j]
            for k in range(4):
                for l in range(1,M):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_num += arr[ni][nj]
            if result < sum_num:
                result = sum_num
        for j in range(N):
            sum_num = 0
            sum_num = arr[i][j]
            for k in range(4):
                for l in range(1,M):
                    nk = i + dk[k] * l
                    nl = j + dl[k] * l
                    if 0 <= nk < N and 0 <= nl < N:
                        sum_num += arr[nk][nl]
            if result < sum_num:
                result = sum_num

    print(f'#{tc} {result}')