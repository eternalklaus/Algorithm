# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        def dfs(node):
            if not node: return
            node.left, node.right = node.right, node.left 
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
        '''
        queue = [root]
        while queue:
            node = queue.pop()
            if not node: continue 
                
            queue.append(node.left)
            queue.append(node.right)
            
            node.left, node.right = node.right, node.left
        return root