T = int(input())

for tc in range(1,T+1):
    N, K = list(map(int,input().split()))
    arr = [(list(map(int,input().split()))+[0])for _ in range(N)]+[[0]*(N+1)]
    f_cnt = 0
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    f_cnt += 1
                cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
                
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    f_cnt += 1
                cnt = 0
    print(f'#{tc} {f_cnt}')