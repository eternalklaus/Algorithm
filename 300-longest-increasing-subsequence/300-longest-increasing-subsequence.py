class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        
        @cache
        def getlongestsub(minimum, idx):
            if idx >= L:
                return 0
            output = 0
            for i in range(idx, L):
                if nums[i] > minimum:
                    output = max(output, 1 + getlongestsub(nums[i], i+1))
            return output 
        
        return getlongestsub(-10**4-1, 0)