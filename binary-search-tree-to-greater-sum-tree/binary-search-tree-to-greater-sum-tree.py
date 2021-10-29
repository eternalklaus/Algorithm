# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # dfs from the rightmost side (reverse order)
        total = 0
        
        def dfs(node):
            if node == None:
                return 
            nonlocal total
            
            lnode = node.left
            rnode = node.right
            # from right side
            dfs(rnode)
            # update value
            total = node.val + total
            node.val = total
            # to left side
            dfs(lnode)
        
        dfs(root)
        return root