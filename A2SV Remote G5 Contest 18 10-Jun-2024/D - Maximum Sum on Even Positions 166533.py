# Problem: D - Maximum Sum on Even Positions - https://codeforces.com/gym/528793/problem/D

for _ in range (int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    if(n==1):
        print(array[0])
        continue
    sum=0
    for i in range (0,n,2):
        sum+=array[i]
    a=[0]
    for i in range (1,n,2):
        a.append(array[i]-array[i-1])
    for i in range (1,len(a)):
        a[i]=max(a[i],a[i]+a[i-1])
    b=[0]
    for i in range(2,n,2):
        b.append(array[i-1]-array[i])
    for i in range (1,len(b)):
        b[i]=max(b[i],b[i]+b[i-1])
    m=max(0,max(a),max(b))
    print(sum+m)