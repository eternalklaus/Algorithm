# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root, '#'])
        if not root: return []

        output = []
        while q:
            node = q.popleft()
            if node == '#':
                if len(q) > 0: q.append('#')
                output.append('#')
                continue 
            else:
                output.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                continue
        
        result = []
        direction = 1
        level = []
        for c in output:
            if c == '#':
                result.append(level[::direction])
                direction *= -1        
                level = []
            else:
                level.append(c)
        return result

            