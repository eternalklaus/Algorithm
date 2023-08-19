class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def getmaxrob(nums):
            cooled, justrobbed = 0, nums[0]    
            for num in nums[1:]: 
                __cooled = max(cooled, justrobbed)
                justrobbed = cooled + num
                cooled = __cooled 
            return max(cooled, justrobbed)
        
        if len(nums) <= 3:
            return max(nums)
        return max(getmaxrob(nums[1:]), getmaxrob(nums[:-1]))
            