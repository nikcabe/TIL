def babygin(p,n):
    for i in range(10):
        if p[i]>=3:
            return n
        if i <=7 and p[i] >= 1 and p [i+1] >= 1 and p[i+2] >=1:
            return n
    else:
        return 0

T = int(input())

for tc in range(1,1+T):
    arr = list(map(int, input().split()))
    a = [0] * 10
    b = [0] * 10

    for i in range(6):
        a[arr[i*2]] += 1
        result = babygin(a,1)
        if result:
            break
        b[arr[i*2+1]] += 1
        result = babygin(b,2)
        if result:
            break
    print(f'#{tc} {result}')