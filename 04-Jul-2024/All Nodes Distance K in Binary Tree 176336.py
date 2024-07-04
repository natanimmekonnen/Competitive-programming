# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
   def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)
        
        visited = set()
        queue = deque([target.val])
        visited.add(target.val)
        
        distance = 0
        
        while queue:
            if distance == k:
                return list(queue)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            
            distance += 1
        
        return []
    
   def buildGraph(self, node, parent, graph):
        if not node:
            return
        
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)