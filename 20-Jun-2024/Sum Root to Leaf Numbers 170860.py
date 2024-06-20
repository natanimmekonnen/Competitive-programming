# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val=[]
        def dfs(root,state):
            if root.left is None and root.right is None:
                val.append( state*10 +root.val)
                return
            if root.left is not None:
                dfs(root.left,state*10+root.val)
            if root.right is not None:
                dfs(root.right,state*10+root.val)
        dfs(root,0)
        return sum(val)
        