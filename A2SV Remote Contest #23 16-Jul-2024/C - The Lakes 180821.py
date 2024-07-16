# Problem: C - The Lakes - https://codeforces.com/gym/535309/problem/C

def dfs(x, y):
    if Lakes[x][y] == 0:
        return 0
    var = set()
    s = 0
    var.add((x, y))
    while len(var) > 0:
        x, y = var.pop()
        s += Lakes[x][y]
        Lakes[x][y] = 0
        if x-1 >= 0:
            if Lakes[x-1][y] > 0:
                var.add((x-1, y))
        if x+1 < n:
            if Lakes[x+1][y] > 0:
                var.add((x+1, y))
        if y-1 >= 0:
            if Lakes[x][y-1] > 0:
                var.add((x, y-1))
        if y+1 < m:
            if Lakes[x][y+1] > 0:
                var.add((x, y+1))
    return s
for _ in range(int(input())):
    n, m = map(int, input().split())
    Lakes = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for x in range(n):
        for y in range(m):
            ans = max(ans, dfs(x, y))
    print(ans)