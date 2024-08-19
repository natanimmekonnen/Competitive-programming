# Problem: C - Hello World - https://codeforces.com/gym/543262/problem/C

x = int(input())
for i in range(x):
    n = int(input())
    y = list(map(int, input().split()))
    y.sort()
    flag = True
    sum = 1
    if y[0] != 1:
        flag = False
    for i in range(1, len(y)):
        if y[i] > sum:
            flag = False
            break
        sum += y[i]
    if flag:
        print("Yes")
    else:
        print("No")
