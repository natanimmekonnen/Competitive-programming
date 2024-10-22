# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def countPrime(n):
    is_prime = [1] * (n+1)
    is_prime[0] = is_prime[1] = 0


    for i in range(2, (n // 2) + 1):
        if is_prime[i]:
            for j in range(i * i, n+1, i):
                is_prime[j] = 0
    return is_prime


def countAlmostPrimes(n):
    num = countPrime(n)
    num2 = 0
    for nums in range(2, n + 1):
        div = 0
        for j in range(2, nums + 1):
            if num[j] and nums % j == 0:
                div += 1
            if div > 2:
                break
        if div == 2:
            num2 += 1
    return num2


n = int(input())
print(countAlmostPrimes(n))
