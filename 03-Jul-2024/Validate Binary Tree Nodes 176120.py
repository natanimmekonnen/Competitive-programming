# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        
        val = [0] * n
        for i in range(n):
            if l[i] != -1:
                val[l[i]] += 1
            if r[i] != -1:
                val[r[i]] += 1
        
        root_count = 0
        root = -1
        for i in range(n):
            if val[i] == 0:
                root_count += 1
                root = i
        
        if root_count != 1:
            return False
        visited = set()
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            if l[node] != -1:
                stack.append(l[node])
            if r[node] != -1:
                stack.append(r[node])
        
        return len(visited) == n
