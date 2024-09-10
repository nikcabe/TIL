def find_set(i):
    while rep[i] != i:
        i = rep[i]
    return i

T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    rep = [i for i in range(N+1)]

    for i in range(M):
        n1,n2 = arr[i*2],arr[i*2+1]
        rep[find_set(n2)] = find_set(n1)

    cnt = 0
    for i in range(1,N+1):
        if rep[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')