# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_g = sum(gas)
        total_c = sum(cost)
    
        if total_g < total_c:
            return -1
        
        start = 0
        current_g = 0
        
        for i in range(len(gas)):
            current_g += gas[i] - cost[i]
            if current_g < 0:
                start = i + 1
                current_g = 0
        
        return start
        