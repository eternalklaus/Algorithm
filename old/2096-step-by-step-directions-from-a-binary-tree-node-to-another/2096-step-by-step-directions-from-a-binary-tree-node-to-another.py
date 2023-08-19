# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find splitting root node 
        # dfs and preorder search the startValue and destValue
        PATH = {'startValue':None, 'destValue':None}
        
        def dfs(node, path):
            if not node: # invalid path 
                return 
            if PATH['startValue'] and PATH['destValue']: # already discovered 
                return
            
            if node.val == startValue:
                PATH['startValue'] = path.copy()
            if node.val == destValue:
                PATH['destValue'] = path.copy()
            
            path.append('L')
            dfs(node.left, path)
            path.pop()
            
            path.append('R')
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        
        # find common prefix of those two values and remove it 
        s, d = PATH['startValue'], PATH['destValue']
        while s and d and s[0] == d[0]:
            s.pop(0)
            d.pop(0)
        
        return 'U' * len(s) + ''.join(d)