# Problem: C - Collecting Game - https://codeforces.com/gym/541399/problem/C


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    sum = 0
    for i in range(n):
        arr.append([a[i], i])
        sum += a[i]
    arr.sort()
    ans = [0] * n
    ans[arr[-1][1]] = n - 1
    sum -= arr[-1][0]
    for i in range(n - 2, -1, -1):
        if sum >= arr[i + 1][0]:
            ans[arr[i][1]] = ans[arr[i + 1][1]]
        else:
            ans[arr[i][1]] = i
        sum -= arr[i][0]
    for i in range(len(ans)):
        print(ans[i], end=' ')
    print()
