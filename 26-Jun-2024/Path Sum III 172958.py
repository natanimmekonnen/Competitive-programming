# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.counter = 0

        def dfs(root, targetSum, currentSum):
            if not root:
                return
            currentSum += root.val
            if currentSum == targetSum:
                self.counter += 1
            dfs(root.left, targetSum, currentSum)
            dfs(root.right, targetSum, currentSum)

        def traverse(root):
            if not root:
                return
            dfs(root, targetSum, 0)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return self.counter
