N = int(input())
arr = list(map(int, input().split()))
max_v = 0
cnt = 1
for i in range(1,N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        if max_v < cnt:
            max_v = cnt
        cnt = 1
else:
    if max_v < cnt:
        max_v = cnt
    cnt = 1
cnt = 1
for j in range(1,N):
    if arr[j-1] >= arr[j]:
        cnt += 1
    else:
        if max_v < cnt:
            max_v = cnt
        cnt = 1
else:
    if max_v < cnt:
        max_v = cnt
    cnt = 1
if len(arr) == 1:
    max_v = 1
print(max_v)