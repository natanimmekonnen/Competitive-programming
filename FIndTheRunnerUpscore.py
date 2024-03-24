if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(arr)
    big=arr[n-1]
    for index in range(n-1,-1,-1):
        if arr[index]!= big:
            print(arr[index])
            break