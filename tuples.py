# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    numbers = map(int, input().split())
    my_tuple = tuple(numbers)
    print(hash(my_tuple))


