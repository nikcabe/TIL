'''
값을 3개를 받는다.
K,N,M
k는 한번 충전에 움직일 수 있는 정류장 수
N은 종점의 번호
M은 충전기가 설치된 정류장
'''
K, N, M = map(int, input().split())
bus_stop = []
bus_charge = []
test = []
for stop in ran
ge(N+1):
    bus_stop.append(stop)
bus_charge = list(map(int,input().split()))
for i in bus_charge:
    bus_stop[i]="o"

print(bus_stop)