# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):
            if node1 and node2:
                output = TreeNode(node1.val + node2.val)
                output.left = dfs(node1.left, node2.left)
                output.right = dfs(node1.right, node2.right)
                return output
            else: # wow we don't need to recurr it.. wow..
                return node1 or node2
        
        return dfs(root1, root2)
                
            