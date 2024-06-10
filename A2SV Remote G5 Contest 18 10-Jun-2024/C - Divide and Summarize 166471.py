# Problem: C - Divide and Summarize - https://codeforces.com/gym/528793/problem/C

n=set()
array=[]
 
def calculate(left,right):
    global n,array
    sum=0
    for i in range(left,right+1):
        sum+=array[i]
    n.add(sum)

    mid=(array[left]+array[right])//2
    pos=-1
    for i in range(left,right+1):
        if array[i]<=mid:
            pos=i
        else:
            break
    if pos==-1 or pos==right:
        return
    calculate(left,pos)
    calculate(pos+1,right)
def solve():
    global array,n
    k,l =map(int,input().split())
    array=list(map(int,input().split()))
    n=set()
    array.sort()
    calculate(0,k-1)
    for _ in range(l):
        x=int(input())

        if x in n:
            print('YES')
        else:
            print('NO')
case=int(input())
while (case>0):
    solve()
    case=case-1