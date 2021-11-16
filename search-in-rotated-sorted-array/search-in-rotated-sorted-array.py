class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def inhere(i1, i2):
            if nums[i1] < nums[i2]: # normal 
                if nums[i1] <= target < nums[i2]: return True 
            else: # abnormal. rotated string 
                if nums[i1] <= target or target < nums[i2]: return True 
            return False 
        
        # binary search
        li, ri = 0, len(nums)
        while li < ri:
            if nums[li] == target:
                return li 

            mi = (li + ri) // 2
            if inhere(li, mi) == True:
                li, ri = li, mi 
            else:
                li, ri = mi, ri
        
        return -1