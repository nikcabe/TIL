T = int(input())

for tc in range(1,1+T):
    arr = list(map(int,input()))
    triple = 0
    strite = 0
    lst = [0]*10
    for _ in arr:
        lst[_] += 1
    i = 0
    while i<10:
        if lst[i] >= 3:
            lst[i] -= 3
            triple+=1
        if lst[i] == 1 and lst[i+1] == 1 and lst[i+2]:
            lst[i]-=1
            lst[i+1]-=1
            lst[i+2]-=1
            strite+=1
        i += 1
    if strite + triple == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose') 