class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sweeping approach 
        mins = [nums[0] for _ in range(len(nums))] # to initialize nums[0] 
        maxs = [nums[0] for _ in range(len(nums))] # to initialize nums[0] 
        
        output = nums[0]
        
        for i in range(1, len(nums)):
            val1 = mins[i-1] * nums[i]
            val2 = maxs[i-1] * nums[i]
            val3 = nums[i]
            mins[i] = min([val1, val2, val3])
            maxs[i] = max([val1, val2, val3])
            output = max(output, maxs[i])
        
        return output 