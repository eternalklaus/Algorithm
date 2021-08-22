class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort! sort! sort!!! 
        nums.sort()
        return sum(nums[::2])