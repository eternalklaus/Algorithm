# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        output = 0
        
        def dfs(node):
            nonlocal output
            if not node: return
            if low <= node.val <= high:
                output += node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return output