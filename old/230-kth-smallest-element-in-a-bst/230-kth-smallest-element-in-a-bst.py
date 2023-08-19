# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        node = root 
        stack = [root]
        while stack: 
            # push left nodes indescreetly
            while node:
                stack.append(node)
                node = node.left 
            
            # pop node gently
            node = stack.pop()
            k -= 1 
            if k == 0: return node.val 
            
            # now move to right node gently
            node = node.right 
        
        return -1
            