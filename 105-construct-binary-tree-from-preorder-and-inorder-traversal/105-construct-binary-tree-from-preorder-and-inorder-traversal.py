# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def buildtree(preorder, inorder):
            # base cases
            if not inorder: return None 
            
            val = preorder.pop(0)
            idx = inorder.index(val)
            linorder, rinorder = inorder[:idx], inorder[idx+1:]
            
            root = TreeNode()
            root.val = val 
            root.left = buildtree(preorder, linorder)
            root.right = buildtree(preorder, rinorder)
            return root 
        
        return buildtree(preorder, inorder)
            
        