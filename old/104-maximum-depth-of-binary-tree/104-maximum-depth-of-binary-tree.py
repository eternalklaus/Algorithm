# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        output = 0
        def dfs(node, lvl):
            nonlocal output 
            if not node: return 
            output = max(output, lvl)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
        
        dfs(root, 1)
        return output 

        