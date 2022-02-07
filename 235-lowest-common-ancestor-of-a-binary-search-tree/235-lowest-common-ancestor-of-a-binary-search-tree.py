# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        output = None
        
        def dfs(node):
            nonlocal output 
            if not node: 
                return False 
            if output:
                return False 
            
            l, r = dfs(node.left), dfs(node.right)
            
            # case 1) p is parant of q
            if node == p or node == q:
                if l or r:
                    output = node 
                    return False 
                else:
                    return True 
            # case 2) p and q are siblings, so return common parant node. 
            if l and r:
                output = node 
                return False 
            # case 3) send True to the parant nodes
            if l or r:
                return True 
            
            return False 
        
        dfs(root)
        return output 