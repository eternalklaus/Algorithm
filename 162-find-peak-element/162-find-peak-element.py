class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search 
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        li, ri = 1, len(nums) - 2
        while li < ri:
            mi = (li + ri) // 2
            if nums[mi-1] < nums[mi] and nums[mi+1] < nums[mi]:
                return mi - 1 
            
            if nums[mi-1] > nums[mi]: # pick left side 
                ri = mi-1
            else: # nums[mi-1] < nums[mi] -> pick right and middle side 
                li = mi+1
        
        return li - 1