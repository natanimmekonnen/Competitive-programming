# Problem: d - Valid BFS? - https://codeforces.com/gym/533316/problem/d

from collections import deque


n = int(input())

graph = [[] for _ in range(n)]
order = [0] * n
queue = deque([0])
visited = set([0])
bfsss = []
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
bfs = list(map(int, input().split()))
bfs = [i-1 for i in bfs]


for j in range(n):
    order[bfs[j]] = j

for s in range(n):
    graph[s].sort(key=lambda x: order[x])


while queue:
    x = queue.popleft()
    bfsss.append(x)
    for s in graph[x]:
        if s not in visited:
            queue.append(s)
            visited.add(s)
if bfsss == bfs:
    print("Yes")
else:
    print("No")
