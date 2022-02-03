# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = defaultdict(list)
        def dfs(node, lvl):
            if not node: return
            output[lvl].append(node.val)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
        
        dfs(root, 0)
        return output.values()