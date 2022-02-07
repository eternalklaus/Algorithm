# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        
        '''
        def serialize(node):
            if not node:
                serial = '#'
            else:
                serial  = '!'
                serial += str(node.val)
                serial += '!'
                serial += serialize(node.left)
                serial += serialize(node.right)
            
            return serial 
        
        if serialize(subRoot) in serialize(root): return True 
        return False 
        '''
        def sy(nd):return f"A{nd.val}#{sy(nd.left)}{sy(nd.right)}"if nd else"Z"
        return sy(subRoot)in sy(root)
                
            
            