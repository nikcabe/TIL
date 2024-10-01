from itertools import combinations

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(n)]

fin_v = 10000
t = list(combinations(p, n//2))
c = len(t)
k = 0
for s1 in t:
	if k == c / 2:
		break
	s = 0
	l = 0
	s2 = list(set(p) - set(s1))
	for i in list(combinations(s1, 2)):
		s += g[i[0]][i[1]]
		s += g[i[1]][i[0]]
	for i in list(combinations(s2, 2)):
		l += g[i[0]][i[1]]
		l += g[i[1]][i[0]]
	tmp = abs(s - l)
	if tmp < fin_v:
		fin_v = tmp
	k += 1
print(fin_v)