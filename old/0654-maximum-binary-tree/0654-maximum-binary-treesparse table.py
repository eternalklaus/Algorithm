# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        L = len(nums)
        nums += [0] * L
        DEFAULT = L

        def getmaxi(i, size):
            # size보다 같거나 작은 2제곱수를 x를 구해 i+x, i+size-x의 맥스중 큰값을 취한다
            if size == 0: return i
            
            x = 2**int(log2(size)) 
            cand1 = sparsetable[(i, x)]
            cand2 = sparsetable.get((i + size - x , x), DEFAULT) ### 디폴트는 값이 0인 인덱스를 리턴한다 
            if nums[cand1] > nums[cand2]:
                return cand1
            return cand2

        sparsetable = {} # {(index,windowsize): maximum value index, ...}
        # 1, 2, 4, 8, ... , 2**log2(nums)
        windowsize = [2**n for n in range(0, int(log2(L))+1)]

        for size in windowsize:
            for i in range(L):
                # 1->2->4... 
                cand1 = getmaxi(i, size-1)
                cand2 = i+size-1
                if nums[cand1] > nums[cand2]:
                    sparsetable[(i,size)] = cand1
                else:
                    sparsetable[(i,size)] = cand2
                
        def buildnode(left, right):
            if left > right:
                return None
            
            i = getmaxi(left, right-left+1)
            node = TreeNode(nums[i])
            node.left = buildnode(left, i-1)
            node.right = buildnode(i+1, right)
            return node
        
        return buildnode(0, L-1)