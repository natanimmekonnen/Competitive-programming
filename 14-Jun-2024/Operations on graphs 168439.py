# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict
n = int(input())
k=int(input())
graph=defaultdict(list)

for i in range(k):
    row=list(map(int,input().split()))
    if row[0]==1:
        u=row[1]
        v=row[2]
        graph[u].append(v)
        graph[v].append(u)
    else:
        print(*graph[row[1]])