# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0:
            return None
        minheap = nums[:k]
        heapq.heapify(minheap)

        for num in nums[k:]:
            if num > minheap[0]:
                heapq.heappushpop(minheap, num)

        return minheap[0]
        