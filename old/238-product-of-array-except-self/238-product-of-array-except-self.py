class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def getmult(except_idx):
            i, output = 0, 1
            while i < len(nums):
                if i != except_idx: 
                    output *= nums[i]
                i += 1
            return output 
          
        # initialize output list 
        output = [0 for _ in range(len(nums))]
        
        if 0 in nums:
            idx = nums.index(0) 
            output[idx] = getmult(idx) # get all muliply except for nums[idx]
        
        else:
            allmult = getmult(-1)
            for i in range(len(nums)):
                output[i] = allmult//nums[i]
                
        return output
        