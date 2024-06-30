# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    ans = ""
    for char in s:
        if char.isupper():
            ans += char.lower()
        elif char.islower():
            ans += char.upper()
        else:
             ans+= char

    return ans
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)