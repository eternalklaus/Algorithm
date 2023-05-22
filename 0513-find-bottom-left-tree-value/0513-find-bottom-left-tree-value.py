# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        # bfs
        output = root
        deque = deque([output])
        while deque:
            node = deque.popleft()
            if node.right:
                output = node.right
                deque.append(node.right) # push right node first,
            if node.left:
                output = node.left
                deque.append(node.left) # and then push left node
        
        return output.val
            
                
        
            