for case in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
 
    for _ in range(dump):
        box_max = box[0]
        box_min = box[0] 
        pos_min = 0
        pos_max = 0 
 
        for i in range(100):
            if box_max < box[i]:
                box_max = box[i]
                pos_max = i
            if box_min > box[i]:
                box_min = box[i]
                pos_min = i
 
        box[pos_max] -= 1
        box[pos_min] += 1
         
    print(f'#{case} {max(box)-min(box)}')