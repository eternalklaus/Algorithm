class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -1 * float('inf')

        '''
        for idx, num in enumerate(nums):
            if idx == 0: 
                currentmax = nums[idx]
                maxsum = nums[idx]
            else:
                currentmax = max(currentmax + nums[idx], nums[idx])
                maxsum = max(maxsum, currentmax)
        
        return maxsum
        '''        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i-1] + nums[i]
            else:
                nums[i] = nums[i]
        return max(nums)