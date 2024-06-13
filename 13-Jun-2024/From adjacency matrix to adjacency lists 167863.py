# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

from collections import defaultdict
n = int(input())
graph=defaultdict(list)
num=1
for i in range(n):
    l=[]
    row=list(map(int,input().split()))
    for j in range(len(row)):
        #graph[i].append((j, row[j]))
        if(row[j]==1):
            graph[i+1].append(j+1)
    
for i,x in  graph.items():
    print(len(x),*x)
    