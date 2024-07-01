# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
    
        visited = [0] * numCourses
    
        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
        
            visited[course] = -1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visited[course] = 1
            return True
    
        for course in range(numCourses):
            if not dfs(course):
                return False
    
        return True
