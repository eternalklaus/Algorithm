class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def minmax(a, b, c):
            return min(a,b,c), max(a,b,c)
        
        max_sofar = nums[0]
        min_sofar = nums[0]
        output    = nums[0]
        
        for i in range(1, len(nums)):
            # use previous calculated value V.S renew the value
            min_sofar, max_sofar = minmax(max_sofar*nums[i], min_sofar*nums[i], nums[i]) # zero-tolerant
            output = max(max_sofar, output) # calculated value until certain point should be taken account
        
        return output
            
        