class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        # n**2까지 줄일순 있겠다. 
        for left in range(len(nums)):
            middle = left + 1
            right = len(nums) - 1
            sum_should_be = -nums[left]
            while middle < right:
                if nums[middle] + nums[right] == sum_should_be:
                    output.add((nums[left], nums[middle], nums[right]))
                    middle += 1
                elif nums[middle] + nums[right] < sum_should_be:
                    middle += 1
                elif nums[middle] + nums[right] > sum_should_be:
                    right -= 1
        return [list(_) for _ in output]
                
