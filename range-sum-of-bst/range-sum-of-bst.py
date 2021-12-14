# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        output = 0
        
        def searchnode(node, minval, maxval):
            nonlocal output 
            # base case
            if node == None: return
            
            # out of range
            if minval > high or maxval < low: return 
            
            lchild = node.left 
            rchild = node.right 
            
            if low <= node.val <= high:
                output += node.val 
            
            searchnode(lchild, minval, node.val)
            searchnode(rchild, node.val, maxval)
        
        
        searchnode(root, low+1, high-1)
        return output 
                