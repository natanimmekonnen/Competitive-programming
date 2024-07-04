# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colVals = defaultdict(list)
        queue = deque([(root, 0, 0)])  

        while queue:
            node, col, row = queue.popleft()
            if node:
                colVals[col].append((row, node.val))
                queue.append((node.left, col - 1, row + 1))
                queue.append((node.right, col + 1, row + 1))
        result = []
        for col in sorted(colVals.keys()):
            colVals[col].sort()  
            result.append([val for row, val in colVals[col]])

        return result
