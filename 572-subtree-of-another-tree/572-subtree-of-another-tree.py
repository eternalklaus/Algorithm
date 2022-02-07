# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        if not subRoot: return True 
        
        @cache 
        def compare(root, subroot):
            if not root and not subroot: 
                return True 
            if root and subroot:
                if root.val == subroot.val:
                    if (compare(root.left, subroot.left) and compare(root.right, subroot.right)): # continue previous one 
                        return True 
                return compare(root.left, subRoot) or compare(root.right, subRoot) # previous compare result or new start      
            return False # None and TreeNode or vice versa
            
        return compare(root, subRoot)
        '''
        
        def checknode(root, subroot):
            if not root and not subroot: return True 
            if root and subroot:
                if root.val == subroot.val:
                    return checknode(root.left, subroot.left) and checknode(root.right, subroot.right)
            return False 
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            
            if not node: continue 
            if checknode(node, subRoot):
                return True
            queue.append(node.left)
            queue.append(node.right)
        return False 
            
            