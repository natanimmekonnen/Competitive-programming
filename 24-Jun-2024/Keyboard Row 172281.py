# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key1 = set("qwertyuiop")
        key2 = set("asdfghjkl")
        key3 = set("zxcvbnm")

        ans = []
        for word in words:
            words = set(word.lower())
            if words.issubset(key1) or words.issubset(key2) or words.issubset(key3):
                ans.append(word)
        return ans