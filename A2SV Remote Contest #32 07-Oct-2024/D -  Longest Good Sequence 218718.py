# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/555625/problem/D

lim = 111111
p = [0] * lim
t = {}
t[1] = [1]
for i in range(2, lim):
    if t.get(i,0) == 0:
        t[i] = [i]
        for j in range(2 * i, lim, i):
        	if j not in t:
        		t[j] = []
        	t[j].append(i)
input()
a = list(map(int, input().split()))
for i in a:
    x = max(p[j] for j in t[i]) + 1
    for j in t[i]:
    	p[j] = x
print(max(p))