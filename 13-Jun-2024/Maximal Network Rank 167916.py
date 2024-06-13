# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # print(roads)
        max_=0
        graph=defaultdict(set)
        for x,y in roads:
            graph[x].add(y)
            graph[y].add(x)
        for i in range(n):
            for j in range(i+1,n):
                sum=len(graph[i])+len(graph[j])
                if j in graph[i] or i in graph[j]:
                    sum=sum-1
                max_=max(max_,sum)
        
        return max_

