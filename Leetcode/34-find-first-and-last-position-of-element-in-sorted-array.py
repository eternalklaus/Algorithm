'''
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
class Solution(object):
    def extreme_insertion_index(self, nums, target, leftbias): 
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] > target or (target == nums[mid] and leftbias): 
                hi = mid 
            else:
                lo = mid + 1
        return lo 

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
     

sl = Solution()
print sl.searchRange([2,2], 3)
# print sl.searchRange([5,7,7,8,8,8,8,10], 8)
# sl.searchRange([], 6)