# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isvalid(minval, node, maxval):
            if not node:
                return True 
            if minval < node.val < maxval:
                return isvalid(minval, node.left, node.val) and isvalid(node.val, node.right, maxval)
            return False 
        
        return isvalid(-2**31-1, root, 2**31)
        