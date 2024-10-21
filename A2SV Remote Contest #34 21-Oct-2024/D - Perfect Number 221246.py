# Problem: D - Perfect Number - https://codeforces.com/gym/559568/problem/D

k = int(input())

n = 19
count = 0
z = 1

while True:
    y = 0
    x = n

    while x > 0:
        y += x % 10
        x //= 10

    if y == 10:
        count += 1
        if count == k:
            print(n)
            break

    z += 1
    n += 1