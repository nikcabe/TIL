T = int(input())

for tc in range(1, 1+T):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        i,j = map(int,input().split())
        for k in range(1, j+1):
            if i-1-k >= 0 and i-1+k <N:
                if arr[i-1-k] == arr[i-1+k]:
                    if arr[i-1-k] == 1:
                        arr[i-1-k], arr[i-1+k] = 0, 0
                    else:
                        arr[i-1 - k], arr[i-1 + k] = 1, 1
    print(f'#{tc}',*arr)