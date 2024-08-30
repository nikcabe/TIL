T = int(input())

for tc in range(1,1+T):
    N = float(input())
    ans = []
    while N != 1:
        N *= 2
        if N > 1:
            N -= 1
            ans.append(1)
        elif N < 1:
            ans.append(0)
        else:
            ans.append(1)
    if len(ans)>12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} ', *ans, sep='')