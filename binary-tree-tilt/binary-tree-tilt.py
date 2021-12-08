# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        output = 0
        
        def getsum(node): # this also returns tilt
            nonlocal output 
            if node == None: 
                return 0 
            
            lsum = getsum(node.left )
            rsum = getsum(node.right)
            output += abs(lsum - rsum) # update output
            return node.val + lsum + rsum # return sum of the subnodes
        
        getsum(root)
        return output
            
            