class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ws = nums.count(1) # window size
        L = len(nums)
        
        
        num0 = nums[0:0+ws].count(0)
        output = num0
        
        nums = nums+nums
        for i in range(1, L):
            if nums[i+ws-1] == 0: # new component is 0! add it!
                num0 += 1
            if nums[i-1] == 0: # passed component was 0.. bye..
                num0 -= 1
            output = min(num0, output)
        return output
            