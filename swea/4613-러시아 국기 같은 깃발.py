T = int(input())

for tc in range(1,1+T):
    N,M = map(int, input().split())
    arr = [input()for _ in range(N)]
    min_v = 9999999
    '''
    포인터 설정이 가장 먼저 온다. 행을 i와 j로 나눴다.
    '''
    for i in range(1,N-1):
        for j in range(i+1,N):
            cnt = 0
            for k in range(i):
                for q in range(M):
                    if arr[k][q] != 'W':
                        cnt += 1
            for k in range(i,j):
                for q in range(M):
                    if arr[k][q] != 'B':
                        cnt += 1
            for k in range(j,N):
                for q in range(M):
                    if arr[k][q] != 'R':
                        cnt += 1
            if min_v > cnt:
                min_v = cnt
    print(f'#{tc} {min_v}')
