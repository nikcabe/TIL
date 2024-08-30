T = int(input())

for tc in range(1,1+T):
    a, b, c = map(int,input().split())
    cnt = 0
    if c <= 2:
        cnt = -1
    elif c <= b:
        cnt += b - c + 1
        b = c-1
        if b <= a:
            cnt += a-b+1
    elif b <= a:
        cnt += a - b + 1
        a = b - 1
    if a < 1 or b < 1 or c < 1:
        cnt = -1
    print(f'#{tc} {cnt}')