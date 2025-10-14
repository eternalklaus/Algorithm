class Solution:
    def search(self, nums: List[int], target: int) -> int:
        li, ri = 0, len(nums)-1
        mi = (li + ri) // 2 
        # li = 3 mi = 3 ri = 4 
        while li < mi and mi < ri:
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                ri = mi
                mi = (li + ri) // 2
            else:
                li = mi
                mi = (li + ri) // 2
        if nums[ri] == target: 
            return ri
        if nums[li] == target:
            return li
        return -1