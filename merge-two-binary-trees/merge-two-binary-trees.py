# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root3 = TreeNode()
        
        def dfs(node1, node2, node3):
            if node1 == None and node2 == None: # no need to continue
                return 
            
            val1, val2 = 0, 0
            if node1: val1 = node1.val
            if node2: val2 = node2.val
            node3.val = val1 + val2
            # print (val1, val2, node3.val)
            
            lchild1 = None if not node1 else node1.left
            rchild1 = None if not node1 else node1.right
            lchild2 = None if not node2 else node2.left
            rchild2 = None if not node2 else node2.right
            
            if lchild1 or lchild2:
                node3.left = TreeNode()
            if rchild1 or rchild2:
                node3.right = TreeNode()
            
            dfs(lchild1, lchild2, node3.left)
            dfs(rchild1, rchild2, node3.right)
        
        if root1 or root2:
            dfs(root1, root2, root3)
            return root3
        else:
            return None