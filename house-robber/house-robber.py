class Solution:
    def rob(self, nums: List[int]) -> int:
        # devide and conquar 
        
        @cache
        def getmax(start):
            if start >= len(nums): 
                return 0
            
            val1 = nums[start] + getmax(start+2)
            val2 = getmax(start+1)
            return max(val1, val2)
        
        return getmax(0)
            