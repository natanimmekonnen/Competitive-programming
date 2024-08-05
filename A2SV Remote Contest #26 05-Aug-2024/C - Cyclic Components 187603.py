# Problem: C - Cyclic Components - https://codeforces.com/gym/540348/problem/C

from collections import  deque
def  bfs(source):
    queue=deque([source])

    visited[source]=1
    booll=True
    while queue:
        curr=queue.popleft()
        if len(graph[curr])!=2:
            booll=False
        for i in graph[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1
    return booll



x,y=map(int,input().split())
visited=[0 for i in range(x)]
val=0
graph=[[] for i in range(x)]
for i in range(y):
    n,m=map(int,input().split())
    graph[n-1].append(m-1)
    graph[m-1].append(n-1)
# print("ho")
for i in range(x):
    if not visited[i] and bfs(i):
        val+=1
        # print("ho")
print(val)