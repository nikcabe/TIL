T = int(input())

for tc in range(1, 1 + T):
    A, B = list(map(str,input().split()))
    i = 0
    cnt = 0
    while i < len(A):
        print(i)
        if A[i:i+len(B)] == B:
            i += len(B)
            cnt += 1
            print(A[i:i+len(B)])
        else:
            cnt += 1
            i += 1    
    print(f'#{tc} {cnt}')