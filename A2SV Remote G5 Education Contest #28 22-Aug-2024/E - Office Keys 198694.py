# Problem: E - Office Keys - https://codeforces.com/gym/543262/problem/E

n,k,p=list(map(int, input().split()))
peop=sorted(list(map(int,input().split())))
key=sorted(list(map(int,input().split())))


def check(x):
    keys=0
    for i in range(n):
        if keys >= k:
            return False
        while abs(peop[i]-key[keys])+abs(p-key[keys])>x:
            keys+=1
            if keys>=k:
                return False
        keys+=1
    return True
left=0
right=int(1e18)
while left< right:
    mid=(left+right)//2
    if check(mid):
        right=mid
    else:
        left=mid+1
print(left)