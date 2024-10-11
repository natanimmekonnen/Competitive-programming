# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap = []
        n = len(costs)
        
        left, right = 0, n - 1
        for i in range(candidates):
            if left <= right:
                heappush(min_heap, (costs[left], left))
                left += 1
            if left <= right:
                heappush(min_heap, (costs[right], right))
                right -= 1
        
        total_cost = 0
        hired = set()
        
        for _ in range(k):
            cost, index = heappop(min_heap)
            
            total_cost += cost
            hired.add(index)
            
            if index < left and left <= right:
                heappush(min_heap, (costs[left], left))
                left += 1
            elif index > right and left <= right:
                heappush(min_heap, (costs[right], right))
                right -= 1
        
        return total_cost
