# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph= defaultdict(list)

        for x,y in edges:
            graph[y].append(x)
            
        ans=[]
        for i in range(n):
            if not graph[i]:
                ans.append(i)
        return ans

        