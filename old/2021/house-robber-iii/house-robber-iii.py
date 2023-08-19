# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        ### Memoization
        memo = {}
        
        def robnode(node, robhere):
            if not node: return 0
            
            # Case 1: cannot rob this node
            if robhere == False: 
                if node in memo and memo[node][0] is not -1: # saved
                    return memo[node][0] 
                
                lmoney = max(robnode(node.left, True),  robnode(node.left, False))
                rmoney = max(robnode(node.right, True), robnode(node.right, False))
                money = lmoney + rmoney
                
                if node not in memo: memo[node] = [-1, -1]
                memo[node][0] = money
            
            # Case 2: rob this node
            else:
                if node in memo and memo[node][1] is not -1: # saved
                    return memo[node][1] 
                
                money = node.val + robnode(node.left, False) + robnode(node.right, False)
                if node not in memo: memo[node] = [-1, -1]
                memo[node][1] = money
            
            return money 
        
        return max(robnode(root, True), robnode(root, False))