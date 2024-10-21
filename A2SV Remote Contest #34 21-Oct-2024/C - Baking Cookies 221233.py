# Problem: C - Baking Cookies - https://codeforces.com/gym/559568/problem/C

def cookies(x, n, k, a, b):
    required_powder = 0
    for i in range(n):
        required = a[i] * x
        if required > b[i]:
            required_powder += required - b[i]
        if required_powder > k:
            return False
    return required_powder <= k

def max_cookies(n, k, a, b):
    low, high = 0, 10**9
    while low <= high:
        mid = (low + high) // 2
        if cookies(mid, n, k, a, b):
            low = mid + 1
        else:
            high = mid - 1
    return high

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_cookies(n, k, a, b))

