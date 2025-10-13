# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs인데 입력값이 반대인... 
        '''
        3 # 9 20 # 15 7 # ... 
        '''
        q = deque([root])
        if not root: return []
        output = []
        direction = 1
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            output.append(level[::direction])
            direction *= -1
        return output