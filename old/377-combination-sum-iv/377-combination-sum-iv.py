class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def combs(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            output = 0
            for num in nums:
                output += combs(target-num)
            return output 
        
        return combs(target)