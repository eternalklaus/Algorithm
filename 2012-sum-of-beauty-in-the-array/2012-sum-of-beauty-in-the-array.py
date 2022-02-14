class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        L, output = len(nums), 0
        mins = [0 for _ in range(L)]
        mins[-1] = nums[-1] # initialize
        
        for i in range(L-2, -1, -1):
            mins[i] = min(mins[i+1], nums[i])
        
        befmax = nums[0]
        for i in range(1, L-1):
            befmax = max(befmax, nums[i-1])
            aftmin = mins[i+1]
            if befmax < nums[i] < aftmin:
                output += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                output += 1
        return output 
        