word1 = input().strip()
word2 = input().strip()
wl1, wl2 = len(word1), len(word2)
cache = [0] * wl2

for i in range(wl1):
    cnt = 0
    for j in range(wl2):
        # cache의 숫자가 cnt보다 큰 경우에 바꿔주세요
        # ACAYKP
        # CAPCAK
        # word1[0]인 A를 검사시에 cache = [0,1,0,0,1,0]
        # 처음으로 마주친 cache의 값 1을 마주치면 다음 올 cache의 값은 2이 된다!

        if cnt < cache[j]:
            cnt = cache[j]
        # 문자가 같다면!
        elif word1[i] == word2[j]:
            # cache를 업데이트!
            cache[j] = cnt + 1

print(max(cache))