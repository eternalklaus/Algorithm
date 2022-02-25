class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        power = [1] * L
        
        for i in range(L):
            for j in range(i):
                if nums[j] < nums[i]: # can update the power
                    power[i] = max(power[i], power[j] + 1)
                    
        return max(power)