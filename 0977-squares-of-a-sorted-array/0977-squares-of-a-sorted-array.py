class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mini = -1
        minval = float('inf')
        for i, num in enumerate(nums):
            nums[i] = num**2
        
        output = [] # 10, 9, 8...
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] > nums[right]:
                output.append(nums[left])
                left += 1
            else:
                output.append(nums[right])
                right -= 1
        return output[::-1]