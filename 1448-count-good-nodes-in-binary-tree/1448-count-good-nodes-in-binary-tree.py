# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxval=-10000) -> int:
        if not root:
            return 0
        
        newmaxval = max(maxval, root.val)
        return int(root.val >= maxval) + self.goodNodes(root.left, newmaxval) + self.goodNodes(root.right, newmaxval)