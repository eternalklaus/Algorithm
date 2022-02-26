class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        power = [1] * L 
        
        for i in range(L):
            for j in range(i):
                if nums[i] > nums[j]:
                    power[i] = max(power[i], 1 + power[j]) 
        return max(power)