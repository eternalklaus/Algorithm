# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def retroot(prerder, inorder):
            if not inorder or not preorder: return None
            rootval = preorder.pop(0)
            
            rootidx = inorder.index(rootval)
            leftchild  = inorder[:rootidx]
            rightchild = inorder[rootidx+1:]
            
            root = TreeNode(rootval) # newly created root node
            root.left = retroot(preorder, leftchild)
            root.right = retroot(preorder, rightchild)
            
            return root
        
        return retroot(preorder, inorder)
            
            