# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # 이전에 나왔던 확실히 안전한 조상을 따로 저장한다. 왜? 현재 노드의 값을 현재 phase에 알 수 없으니까..현재페이즈에서 커버하긴 머리 아프니까..!
        succ = None
        node = root
        while node:
            if node.val > p.val:
                succ = node
                node = node.left
            else:
                node = node.right
        return succ