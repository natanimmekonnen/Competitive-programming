# Problem: Milena and Admirer - https://codeforces.com/problemset/problem/1898/B

import math

t = int(input())
for i in range(t):
    length = int(input())
    array = list(map(int, input().split()))

    num = 0
    for i in range( - 2, -(length+1), -1):
        if array[i] > array[i + 1]:
            val = math.ceil(array[i] / array[i + 1])

            num += val - 1
            array[i] = array[i] //val
            # print(array[i])

    print(num)