# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if node is empty, push 10**4+1
        INV = 10**4+1
        def createlist(root):
            output = []
            queue = [root]
            while queue:
                node = queue.pop(0)
                if not node:
                    output.append(INV)
                    continue 
                output.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            return output 
        
        plist = createlist(p)
        qlist = createlist(q)
        return plist==qlist