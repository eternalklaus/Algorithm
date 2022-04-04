# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # from the root, recort maximum value until reach to the node 
        # dfs since maxval is depend on the path from root to node. 
        output = 0
        
        def dfs(node, maxval):
            nonlocal output 
            if not node: return 
            if node.val >= maxval: ###TODO!! it not needto be always increasing. 3,1,5 would be possible
                output += 1
            maxval = max(node.val, maxval)
            dfs(node.left, maxval)
            dfs(node.right, maxval)
            
        dfs(root, -10**4-1)
        return output 