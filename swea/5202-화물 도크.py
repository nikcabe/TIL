T = int(input())

for tc in range(1,1+T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    arr.sort(key=lambda x:x[1])
    cnt = 0
    end = -1
    for dock in arr:
        if dock[0] >= end:
            cnt += 1
            end = dock[1]

    print(f'#{tc} {cnt}')