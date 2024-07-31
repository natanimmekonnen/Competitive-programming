# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

def find_max_odd_sum(arr):
    possum = sum(x for x in arr if x > 0)
    odd_candidates = [x for x in arr if x % 2 != 0]

    if possum % 2 != 0:
        return possum

    smallest_odd_adjustment = odd_candidates[0]
    for num in odd_candidates:
        if abs(num) < abs(smallest_odd_adjustment):
            smallest_odd_adjustment = num

    return possum - abs(smallest_odd_adjustment)

n = int(input())
arr = list(map(int, input().split()))

result = find_max_odd_sum(arr)

print(result)
