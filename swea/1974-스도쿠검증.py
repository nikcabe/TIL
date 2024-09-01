T = int(input())

for tc in range(1,1+T):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = 0
    for i in range(9):
        sdk = set()
        for j in range(9):
            sdk.add(arr[i][j])
            if len(sdk) == 9:
                result += 1
    for i in range(9):
        sdk = set()
        for j in range(9):
            sdk.add(arr[j][i])
            if len(sdk) == 9:
                result += 1
    i,j = 0,0
    while i != 9:
        for j in range(3):
            sdk = set()
            for k in range(3):
                for l in range(3):
                    sdk.add(arr[i+k][j*3+l])
            if len(sdk) == 9:
                result += 1
        i += 3
    if result == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')