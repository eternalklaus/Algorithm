# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def maxheight(node):
            if node == None: return 0
            lnode = node.left
            rnode = node.right
            return max(maxheight(lnode), maxheight(rnode)) + 1

        def balanced(node):
            if node == None: return True
            lnode = node.left
            rnode = node.right
            if balanced(lnode) and balanced(rnode):
                if abs(maxheight(lnode)-maxheight(rnode)) <= 1:
                    # print (node.val, "True")
                    return True
            # print (node.val, "False")
            return False

        return balanced(root)
    