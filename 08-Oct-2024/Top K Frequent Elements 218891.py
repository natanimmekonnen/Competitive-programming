# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        
        bucket = [[] for _ in range(n + 1)]
        
        for num in freq:
            count = freq[num]
            bucket[count].append(num)
        
        res = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if not k:
                    break
            if not k:
                break
        
        return res
