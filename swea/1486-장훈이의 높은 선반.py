def recur(sum_height,cnt):
    global min_height

    if sum_height >= B:

        min_height = min(min_height, sum_height)
        return


    if cnt == N:
        return


    recur(sum_height+arr[cnt], cnt+1)

    recur(sum_height, cnt+1)


T = int(input())

for tc in range(1,1+T):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    min_height = N*100000+1
    recur(0, 0)
    print(f'#{tc} {min_height-B}')