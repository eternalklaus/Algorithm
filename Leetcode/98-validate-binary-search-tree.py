# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    self.leftmostval    = -(2 ** 31) - 1
    self.rightmostval   = 2 ** 31
    def dfscheck(self, node, bottom, top):
        if node is None: 
            return 
        if bottom < node.val < top:
            self.dfscheck(node.left,  bottom,   node.val)
            self.dfscheck(node.right, node.val, top)
        else:
            return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        