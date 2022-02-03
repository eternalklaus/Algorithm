# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # devide and conquar
        # try preorder search from the left of node, 
        # and if we fill the count, return the node's value immidiatly
        
        output, counter = -1, 0
        
        def inorder(node):
            nonlocal output, counter 
            if not node: return 
            
            inorder(node.left) 
            ###
            # print (node.val, counter)
            counter += 1
            if counter == k: 
                output = node.val 
                return 
            ###
            inorder(node.right)
        
        inorder(root)
        return output 