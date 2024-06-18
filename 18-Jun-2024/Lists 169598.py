# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in Range(N):
        command=input().split()
        if 'insert' in command:
            arr.insert(int(command[1], int(command[2])))
        elif 'print' in command:
            print(arr)
        elif 'remove' in command:
            arr.remove(int(command[1]))
        elif 'append' in command:
            arr.append(int(command[1]))
        elif 'pop' in command:
            arr.pop()
        elif 'reverse' in command:
            arr.reverse()
        elif 'sort' in command:
            arr.sort
    