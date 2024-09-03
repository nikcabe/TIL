T = int(input())

for tc in range(1,1+T):
    n,m = map(int,input().split())
    con = list(map(int, input().split()))
    trk = list(map(int, input().split()))
    con.sort(reverse=True)
    trk.sort(reverse=True)
    i,j =0,0
    result = 0
    while i<n and j<m:
        if con[i] <= trk[j]:
            result += con[i]
            i += 1
            j += 1
        else:
            i += 1
    print(f'#{tc} {result}')

