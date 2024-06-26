# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        grandp=1
        parent=root.val
        vals=[]
        def traverse(root,grandp,parent):
            if root is None:
                return 
            if grandp%2==0:
                vals.append(root.val)
            traverse(root.left,parent,root.val)
            traverse(root.right,parent,root.val)
        traverse(root,grandp,1)
        return sum(vals)