# Problem: D - Xor-tree - https://codeforces.com/gym/531416/problem/D

import sys,threading
def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        x, y = list(map(int, input().split()))
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    visited = set()
    op = []

    def traverse(root, even_op, i, odd_op):
        if even_op % 2 and i % 2 == 0:
            a[root] = 1 - a[root]
        if odd_op % 2 and i % 2 == 1:
            a[root] = 1 - a[root]
        if a[root] != b[root]:
            if i % 2:
                odd_op += 1
            else:
                even_op += 1
            op.append(root + 1)
        visited.add(root)
        for j in graph[root]:
            if j not in visited:
                traverse(j, even_op, i + 1, odd_op)

    traverse(0, 0, 0, 0)
    print(len(op))
    for i in op:
        print(i)
sys.setrecursionlimit(1<<30)
threading.stack_size(1<<27)
main_thread=threading.Thread(target=main)
main_thread.start()
main_thread.join()
