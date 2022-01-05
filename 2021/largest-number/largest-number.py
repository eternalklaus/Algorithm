class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(reverse = True)
        
        total = len(nums)
        for i in range(total):
            for j in range(i+1, total):
                if nums[i][0] != nums[j][0]: break 
                if nums[i]+nums[j] < nums[j]+nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        
        output = ''.join(nums)
        if nums[0] == '0': return '0'
        else: return output