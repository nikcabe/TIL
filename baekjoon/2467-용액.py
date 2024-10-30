n = int(input())
arr = list(map(int,input().split()))
value = 2000000000
l = 0
r = n-1
x, y =0,0

while l < r:
    sum_val = arr[l] + arr[r]

    if abs(sum_val) <= abs(value):
        x = arr[l]
        y = arr[r]
        value = sum_val

    if sum_val <= 0:
        l += 1

    else:
        r -= 1

print(x,y)
