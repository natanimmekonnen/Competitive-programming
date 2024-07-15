# Problem: D - Heap Operations - https://codeforces.com/gym/535309/problem/D

from heapq import *

n = int(input())
heap = []
op = []
for i in range(n):
    v = input().rstrip()
    if v[0] == 'i':
        X = int(v.split()[1])
        heappush(heap, X)
        op.append(v)
        continue
    if v[0] == 'g':
        X = int(v.split()[1])
        while heap and heap[0] < X:
            heappop(heap)
            op.append("removeMin")
        if not heap or heap[0] > X:
            op.append("insert " + str(X))
            heappush(heap, X)
        op.append(v)
        continue

    if not heap:
        op.append("insert 1")
    else: heappop(heap)
    op.append(v)
print(len(op))
print("\n".join(op))