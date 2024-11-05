# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        gr = defaultdict(set)
        for p in prerequisites:
            gr[p[1]].add(p[0])
        
        memo = {}
        def dfs(curr, target):
            if (curr, target) in memo:
                return memo[(curr, target)]
            if curr == target:
                memo[(curr, target)] = True
                return True
            else:
                for child in gr[curr]:
                    if dfs(child, target):
                        memo[(curr, target)] = True
                        return True
            memo[(curr, target)] = False
            return False
        res = []
        for i in range(len(queries)):
            res.append(dfs(queries[i][1], queries[i][0]))
        return res
        