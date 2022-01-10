class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        # 4 5 6 6 1 [1] 2 3 4
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] == target: 
                return True 
            
            # [case 1] left is rotated
            if nums[lo] > nums[mi]:
                if target >= nums[lo] or target < nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            
            # [case 2] right is rotated
            elif nums[mi] > nums[hi]: 
                if target > nums[mi] or target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
            
            # [case 3] left is straightforward
            elif nums[lo] < nums[mi]:
                if nums[lo] <= target < nums[mi]:
                    hi = mi - 1
                else: 
                    lo = mi + 1
            
            # [case 4] right is straighforward
            elif nums[mi] < nums[hi]:
                if nums[mi] < target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1

            # [case 5] cannot be defined!!!
            # ex) 1 0 [1] 1 1
            #     -    -    -
            #     lo   mi   hi
            else: 
                hi -= 1
                lo += 1 
            
        if nums[lo] == target: 
            return True 
        return False
                