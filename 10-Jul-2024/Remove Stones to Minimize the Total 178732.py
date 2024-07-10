# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = [-i for i in piles] 
        heapify(n)

        for _ in range(k):
            m = -heappop(n)
            m -= m//2
            heappush(n, -m)

        return -sum(n)
        