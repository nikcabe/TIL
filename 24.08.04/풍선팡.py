T = int(input())

for tc in range(1,1+T):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    final_v = 0
    for i in range(N):
        for j in range(M):
            max_v = 0
            max_v += arr[i][j]
            for k in range(4):
                ni = i+di[k]
                nj = i+dj[k]
                if 0<= ni < N and 0<= nj < N:
                    max_v += arr[ni][nj]
                print(max_v)
        if max_v > final_v:
            final_v = max_v
    print(f'#{tc} {final_v}')