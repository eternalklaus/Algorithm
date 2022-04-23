# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxval = -10**4 - 1) -> int:
        if not root: return 0
        maxval2 = max(maxval, root.val)
        return int(root.val >= maxval) + self.goodNodes(root.left, maxval2) + self.goodNodes(root.right, maxval2)
        '''
        output = 0
        
        def dfs(node, maxval):
            nonlocal output 
            if not node: return 
            if node.val >= maxval: # this node is a good node 
                output += 1
                
            maxval = max(maxval, node.val)
            dfs(node.left, maxval)
            dfs(node.right, maxval)
        
        
        dfs(root, -10**4 - 1)
        return output
        '''