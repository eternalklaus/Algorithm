# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serial(node):
            if not node: return '#'
            return f'|{node.val}|{serial(node.left)}|{serial(node.right)}'
        return serial(subRoot) in serial(root)