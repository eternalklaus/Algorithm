# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        levels = defaultdict(list)
        
        def getlevel(node):
            # base cases 
            if not node:
                return -1 ###<- always emit the level
            
            if not node.left and not node.right:
                lv = 0
            else:
                lv = max(getlevel(node.left), getlevel(node.right)) + 1
            
            levels[lv].append(node.val)
            return lv
        
        getlevel(root)
        return levels.values()
            