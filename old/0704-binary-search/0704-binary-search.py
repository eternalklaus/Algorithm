class Solution:
    def search(self, nums: List[int], target: int) -> int:
        li, ri = 0, len(nums)-1

        while li <= ri:
            mi = (li + ri) // 2
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                ri = mi - 1
            else:
                li = mi + 1
        return -1