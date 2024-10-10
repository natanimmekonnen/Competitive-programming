# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())


def merge(left, right, x):
    if left == -1 or right == -1:
        return [-1, x]

    if left[-1] <= right[0]:
        return [left + right, x]
    elif right[-1] <= left[0]:
        return [right + left, x + 1]
    else:
        return [-1, x]


def mergeSort(array, steps):
    if len(array) <= 1:
        return [array, steps]
    if array == -1:
        return [array, steps]

    mid = len(array) // 2

    left = mergeSort(array[:mid], 0)
    right = mergeSort(array[mid:], 0)
    return merge(left[0], right[0], left[1] + right[1] + steps)


for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    res= mergeSort(array, 0)
    if res[0] == -1:
        print(res[0])
    else:
        print(res[1])
