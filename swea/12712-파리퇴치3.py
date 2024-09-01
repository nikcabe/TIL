T = int(input())

for tc in range(1,1+T):
    n,m = map(int,input().split())
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    dk = [1,1,-1,-1]
    dl = [1,-1,-1,1]
    arr = [list(map(int,input().split()))for _ in range(n)]
    max_v = 0
    for i in range(n):
        for j in range(n):
            sum_v = 0
            sum_v = arr[i][j]
            for k in range(4):
                for l in range(1,m):
                    ni = i+di[k] * l
                    nj = j+dj[k] * l
                    if 0 <= ni < n and 0 <= nj <n:
                        sum_v += arr[ni][nj]
            if max_v < sum_v:
                max_v = sum_v
        for j in range(n):
            sum_v = 0
            sum_v = arr[i][j]
            for k in range(4):
                for l in range(1,m):
                    nk = i+dk[k] * l
                    nl = j+dl[k] * l
                    if 0 <= nk < n and 0 <= nl <n:
                        sum_v += arr[nk][nl]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')