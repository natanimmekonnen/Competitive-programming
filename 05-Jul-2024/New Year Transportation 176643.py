# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A


n, t = map(int, input().split())
portals = list(map(int, input().split()))

current_position = 1


while current_position < t:
    current_position += portals[current_position - 1]
    
    if current_position == t:
        print("YES")
        break
else:
   
    print("NO")
