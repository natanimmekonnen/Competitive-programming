# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/555625/problem/C

def ispali(num):
    original, reversed_num = num, 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num


def palindrome(val):
    palindromes = []
    for num in range(1, val + 1):
        if ispali(num):
            palindromes.append(num)
    return palindromes


def subset(palindromes, max_sum, mod):
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    for num in palindromes:
        for i in range(num, max_sum + 1):
            dp[i] = (dp[i] + dp[i - num]) % mod
    return dp


limit = 40001
mod = 1000000007
palindromes = palindrome(limit)

max = 40001
dp = subset(palindromes, max, mod)

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
