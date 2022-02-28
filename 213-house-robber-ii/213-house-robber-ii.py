class Solution:
    def rob(self, nums: List[int]) -> int:
        # if we rob first nums, we should cool down at last session.  
        # so take two cases, nums, and nums[:-1]
        
        if len(nums) <= 3: # 1 or 2 or 3
            return max(nums)
        
        
        # robbed first house
        justrobbed, cooled = nums[0]+nums[2], nums[0]
        for num in nums[3:-1]:
            __cooled = max(justrobbed, cooled)
            justrobbed = cooled + num    
            
            cooled = __cooled 
        output1 = max(justrobbed, cooled)
        
        # didn't robbed first house
        justrobbed, cooled = nums[1], 0
        for num in nums[2:]:
            __cooled = max(cooled, justrobbed)
            justrobbed = cooled + num
            
            cooled = __cooled 
        output2 = max(justrobbed, cooled)
        
        return max(output1, output2)