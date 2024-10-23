N, K = map(int, input().split())
# 더미 데이터 생성
stuff = [[0,0]]
# 표를 생성 knap[i][j]에서 i번째 아이템을 의미, j는 무게를 의미
knap = [[0 for _ in range(K+1)] for _ in range(N+1)]

# 입력 받은 물건 데이터를 리스트에 저장
for _ in range(N):
    stuff.append(list(map(int,input().split())))


for i in range(1,N+1):
    weight = stuff[i][0]
    value = stuff[i][1]
    for j in range(1,K+1):
        if j < weight:
            # 현재 무게 j 가 아이템의 무게보다 작으면 아이템을 포함할 수 없다.
            knap[i][j] = knap[i-1][j]
        else:
            # 현재 아이템을 포함할 수 있는 경우 아이템을 추가 했을 떄와 추가하지 않았을 때 더 큰 값을 넣는다.
            knap[i][j] = max(value+knap[i-1][j-weight],knap[i-1][j])

print(knap[N][K])