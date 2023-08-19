class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,0,1,1,4]
        canreach = 0
        for i, num in enumerate(nums):
            if i > canreach:
                return False 
            canreach = max(canreach, i + num)
        
        return True 
        
        