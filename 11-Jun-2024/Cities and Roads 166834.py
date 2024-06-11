# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

from collections import defaultdict

n = int(input())

count = 0
graph = defaultdict(list)

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        graph[i].append((j, row[j]))
        if row[j] == 1:  
            count += 1

print(count//2)
