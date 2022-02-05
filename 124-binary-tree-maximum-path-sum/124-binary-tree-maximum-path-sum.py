# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        output = root.val
        
        def getmaxval(node):
            nonlocal output
            if not node: return 0
            
            lchildmax = getmaxval(node.left)
            rchildmax = getmaxval(node.right) 
            output = max([output ,lchildmax+rchildmax+node.val, lchildmax+node.val, rchildmax+node.val, node.val])
            
            return max(lchildmax+node.val, rchildmax+node.val, node.val)
        
        getmaxval(root)
        return output 