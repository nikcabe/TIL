T = int(input())

for tc in range(1,1+T):
    K,N,M = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    bus_stops = [0]*(N+1)
    for i in arr:
        bus_stops[i]+=1

    bus = 0
    cnt = 0

    while bus+K < N:
        #가장 먼 충전기의 위치를 저장해주기 위한 변수
        charge = 0          

        for i in range(bus+1,bus+1+K):
            #최대 정거장 안에 충전소가 있는 지 확인
            if i<N and bus_stops[i] == 1: 
                charge = i
        if charge == 0:
            cnt = 0
            break

        bus = charge
        cnt += 1
    
    print(f'{tc} {cnt}')