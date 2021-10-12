class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -1 * float('inf')
        
        @cache
        def getmaxsum(idx):
            nonlocal maxsum
            
            if idx == -1: return 0
            
            a = getmaxsum(idx-1) + nums[idx]
            b = nums[idx] 
            output = max(a, b)
            maxsum = max(maxsum, output)
            return output
        
        for idx, _ in enumerate(nums):
            getmaxsum(idx)
        
        return maxsum