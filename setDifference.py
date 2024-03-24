# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_students = input()
rollno = set(map(int, input().split()))
fren_students = input()
rollno2= set(map(int,input().split()))
print(len(rollno.difference(rollno2)))