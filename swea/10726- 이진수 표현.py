T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())
    lst = bin(M)[2:]
    lst = lst.zfill(N)
    if '0' in lst[-N:]:
        print(f'#{tc} OFF')
    else:
        print(f'#{tc} ON')