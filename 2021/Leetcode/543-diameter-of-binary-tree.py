# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter = 0        
        def longest_path(node):
            nonlocal diameter

            if not node: 
                return -1

            else: 
                lnodelen = longest_path(node.left)
                rnodelen = longest_path(node.right)
                diameter = max(lnodelen + rnodelen + 2, diameter)
                return max(lnodelen+1, rnodelen+1)
        
        longest_path(root)
        return diameter
