# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

n=input()
stack=[]
count=0
for i, char in enumerate(n):
    # print(i , char)
    if char == '(':
        stack.append(i)
    else:
        if stack and n[stack[-1]] == '(':
            stack.pop()
            count+=2
        else:
            stack.append(i)


print(count)