class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [0 for x in range(N)]
        
        if nums.count(0) >= 2:
            return output
        
        if nums.count(0) == 1:
            product = 1
            
            for n in nums:
                if n == 0: continue
                product *= n
            
            idx = nums.index(0)
            output[idx] = product

            return output
        
        else: 
            product = 1
            for n in nums:
                product *= n
            
            for idx, k in enumerate(output):
                output[idx] = int(product / nums[idx])
            
            return output