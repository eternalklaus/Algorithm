class Solution:
    def search(self, nums: List[int], target: int) -> int:
        li, ri = 0, len(nums) - 1
        while li < ri:
            # 5 6 7 1 2 3 4
            mi = (li + ri) // 2
            if nums[mi] == target: return mi 

            # left is rotated
            if nums[li] > nums[mi]:
                if target >= nums[li] or target < nums[mi]:
                    li = li
                    ri = mi - 1
                else:
                    li = mi + 1
                    ri = ri 

            # right is rotated
            elif nums[mi] > nums[ri]:
                if target > nums[mi] or target <= nums[ri]:
                    li = mi + 1
                    ri = ri 
                else:
                    li = li
                    ri = mi - 1 

            # no part is rotated either
            else:
                if nums[mi] < target <= nums[ri]:
                    li = mi + 1
                    ri = ri 
                else:
                    li = li 
                    ri = mi - 1
        
        if nums[li] == target:
            return li 
        return -1