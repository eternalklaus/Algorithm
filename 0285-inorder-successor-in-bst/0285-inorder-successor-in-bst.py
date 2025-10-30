# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        heap = []
        def traverse(node):
            nonlocal heap
            if node == None: return 
            if node.val > p.val:
                heapq.heappush(heap, (node.val, node))
            traverse(node.left)
            traverse(node.right)
        traverse(root)

        if not heap: return None
        (_, node) = heappop(heap)
        return node