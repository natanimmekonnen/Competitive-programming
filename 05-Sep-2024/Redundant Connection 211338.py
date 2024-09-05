# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents=[i for i in range(len(edges)+1)]
        ranks= [1]* (len(edges)+1)

        def find(x):
            p=parents[x]
            while p!=parents[p]:
                parents[p]=parents[parents[p]]
                p=parents[p]
            return p
        def union(x1,x2):
            p1,p2=find(x1),find(x2)
            if p1==p2:
                return False
            if ranks[p1]>ranks[p2]:
                parents[p2]=p1
                ranks[p1]+= ranks[p2]
            else:
                parents[p1]=p2
                ranks[p2]+= ranks[p1]
            return True
        for x1,x2 in edges:
            if not union(x1,x2):
                return [x1,x2]

        