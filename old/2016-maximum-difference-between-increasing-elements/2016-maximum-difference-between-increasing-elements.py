class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        L = len(nums)
        minval, maxdiff = nums[0], nums[1]-nums[0]
        
        for num in nums[1:]:
            maxdiff = max(maxdiff, num - minval)
            minval = min(minval, num) # update minval
        
        if maxdiff > 0:
            return maxdiff 
        return -1