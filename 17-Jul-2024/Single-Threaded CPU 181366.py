# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(v, process, i) for i, (v, process) in enumerate(tasks)]
        tasks.sort()
        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or min_heap:
            while i < n and tasks[i][0] <= time:
                v, process, index = tasks[i]
                heapq.heappush(min_heap, (process, index))
                i += 1
            
            if min_heap:
                process, index = heapq.heappop(min_heap)
                result.append(index)
                time += process
            else:
                time = tasks[i][0]
        
        return result


        