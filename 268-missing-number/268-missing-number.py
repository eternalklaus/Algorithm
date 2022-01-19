class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = len(nums)
        nums.sort()
        for i in range(L):
            if nums[i] != i:
                return i
        return L