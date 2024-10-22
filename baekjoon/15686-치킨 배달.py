from itertools import combinations

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        # 모든 치킨 집과 대조
        for j in range(m):
            # 초기값과 집에서 치킨집까지의 거리 중 최소값으로 초기값을 선택
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        # 거리의 치킨거리로 저장
        temp += chi_len
    result = min(result, temp)

print(result)