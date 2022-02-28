class Solution:
    def rob(self, nums: List[int]) -> int:
        # justrobbed -> cooled 
        # cooled -> cooled / justrobbed 
        output = 0
        justrobbed = nums[0]
        cooled = 0
        
        for num in nums[1:]:
            __cooled = max(cooled, justrobbed)
            justrobbed = cooled + num
            
            cooled = __cooled
        return max(justrobbed, cooled)