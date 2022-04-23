# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxval = -10**4 - 1) -> int:
        def dfs(node, maxval):
            if not node: return 0
            
            maxval2 = max(maxval, node.val)
            return int(node.val >= maxval) + dfs(node.left, maxval2) + dfs(node.right, maxval2)
            
        
        return dfs(root, -10**4 - 1)
        
        