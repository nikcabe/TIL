T = int(input())

for tc in range(1,1+T):
    P, Q, R, S, W = map(int,input().split())
    A = W*P
    B = 0
    if W <= R:
        B = Q
    else:
        B = (W-R)*S + Q
    print(f'#{tc} {min(A,B)}')