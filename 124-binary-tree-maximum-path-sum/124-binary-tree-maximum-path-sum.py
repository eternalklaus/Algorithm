# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # can we collect more then 3 nodes?
        output = root.val 

        # inorder search and collect the maxinum value in node 
        def inorder(node):
            nonlocal output 
            if not node: return 0
            
            # we can take only one among the two subway
            lval = inorder(node.left) 
            rval = inorder(node.right) 
            ival = node.val 
            
            currentmax = max([ival, ival+lval, ival+rval, ival+lval+rval])
            output = max(output, currentmax)
            
            return max([lval+node.val, rval+node.val, node.val]) # follow left/right or not follow either. 

        inorder(root)
        return output 