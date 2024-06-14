# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        path = []
        n = len(num)

        def backTrack(i):
            length = len(path)
            if i >= n:
                for k in range(2, length):
                    if path[k] != path[k - 1] + path[k - 2]:
                        return False
                return length >= 3
            for j in range(i, n):
                arr = num[i : j + 1]
                if arr[0] == '0' and len(arr) > 1 :
                    return False
                numb = int(arr)
                if length <= 2 or numb == path[len(path)-2] + path[len(path)-1]:
                    path.append(numb)
                    if backTrack(j + 1):
                        return True
                    path.pop()
            return False

        return backTrack(0)
