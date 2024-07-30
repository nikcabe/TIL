	
T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bus_stops = [0] * (n+1)
    for i in arr:
        bus_stops[i] += 1

    bus, cnt =0
    while bus+k < n:
        charge  = 0
        for i in range(bus+1,bus+k+1):
            if i <= n and charge[i] == 1:
                charge = i
            if charge == 0:
                count = 0
                break
        bus = charge
        cnt += 1
    print(f'#{test_case} {cnt}')


# now = 0
# i = 1
# charge = 0

# while now < i <= m+1:
#     if arr[i] - arr[now] > k:
#         if i - now == 1:
#             charge = 0
#             break
#         now = (i - 1)
#         charge += 1
#     else:
#         i += 1

# print(f'#{test_case} {charge}')