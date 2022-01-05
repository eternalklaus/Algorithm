# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    bottom = -(2**31)-1
    def inorder(self, node):
        lresult = mresult = rresult = True 
        
        if node.left is not None:
            lresult = self.inorder(node.left)
        
        mresult = self.bottom < node.val 
        self.bottom = node.val
        
        if node.right is not None:
            rresult = self.inorder(node.right)

        return lresult & mresult & rresult

    def isValidBST(self, root):
        return self.inorder(root) 

        