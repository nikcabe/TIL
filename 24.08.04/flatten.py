for tc in range(1,11):
    dump = int(input())
    arr = list(map(int,input().split()))

    for i in range(dump):
        max_v = arr[0]
        min_v = arr[0]
        max_idx = 0
        min_idx = 0

        for j in range(100):
            if max_v < arr[j]:
                max_v = arr[j]
                max_idx = j
            if min_v > arr[j]:
                min_v = arr[j]
                min_idx = j

        arr[max_idx]-=1
        arr[min_idx]+=1
    final_max = 0
    final_min = arr[0]
    for val in arr:
        if final_max < val:
            final_max  = val
        if final_min > val:
            final_min = val
    print(final_max-final_min)