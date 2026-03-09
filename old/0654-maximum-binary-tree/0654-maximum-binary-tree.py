# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        L = len(nums)
        # isort = sorted(list(range(L)), key = lambda i:nums[i], reverse=True)
        # print (isort)
        # 가장큰거 픽
        # 왼쪽, 오른쪽 자식에 프리픽스 넣음
        def create_node(left, right): # left 포함, right 미포함
            if left == right: return None
            maxval, maxi = -1, -1
            for i in range(left, right):
                if nums[i] > maxval:
                    maxi = i
                    maxval = nums[i]
            node = TreeNode(maxval)
            node.left = create_node(left, maxi)
            node.right = create_node(maxi+1, right)
            return node
        return create_node(0, L)