# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = []
        output = 0
        
        def adventure(node):
            nonlocal stack, output 
            if not node: return
            
            # update output 
            stack.append(node.val)
            diff = max(stack) - min(stack)
            output = max(diff, output)
            
            # recursive call and go to adventure
            adventure(node.left)
            adventure(node.right)
            stack.pop()
            
        
        adventure(root)
        return output 