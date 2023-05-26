# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        heap = deque([root])
        output = root
        
        while heap:
            node = heap.popleft()
            output = node           
            heap += filter(None, [node.right, node.left])
        
        return output.val
            