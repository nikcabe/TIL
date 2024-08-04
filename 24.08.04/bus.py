T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [0]*5001
    for _ in range(N):
        A, B = list(map(int,input().split()))
        for i in range(A,B+1):
            arr[i]+=1
            
    P = int(input())
    lst = [0]*P
    for _ in range(P):
        lst[_] = int(input())
    print(f'#{tc}', end = ' ')
    for i in lst:
        print(arr[i], end=' ')
