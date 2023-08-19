class Solution(object):
    def findPeakElement(self, nums):
        nums.insert(0, -float('inf'))
        nums.append(-float('inf'))
        li, ri = 1, len(nums)-2 
        while li < ri:
            mi = (li + ri)//2
            if nums[mi] > nums[mi-1] and nums[mi] > nums[mi+1]:
                return mi - 1
            if nums[mi-1] > nums[mi]: # pick left side 
                ri = mi - 1
                continue 
            if nums[mi+1] > nums[mi]: # pick right side 
                li = mi + 1
                
        return li - 1
        