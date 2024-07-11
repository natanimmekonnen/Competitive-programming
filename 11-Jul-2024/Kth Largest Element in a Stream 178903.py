# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums[:k]
        heapq.heapify(self.minheap)
        
        for num in nums[k:]:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif val > self.minheap[0]:
            heapq.heappushpop(self.minheap, val)
        
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
