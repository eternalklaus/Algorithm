class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canreach = 0
        for i, num in enumerate(nums):
            if i > canreach:
                return False 
            canreach = max(canreach, i+num)
        return True