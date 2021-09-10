class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N, zeros, product = len(nums), nums.count(0), 1
        output = [0 for x in range(N)]
        
        # if more then 2 zeros, all would be zero
        if zeros >= 2:
            return output
        
        # if 1 zero exist, all output except for output[nums.index(0)] would be zero
        elif zeros == 1:
            for n in nums:
                if n == 0: continue
                product *= n
            output[nums.index(0)] = product
            return output
        
        # else, lets get output by (multiplication of all) / nums[i]
        else: 
            for n in nums:
                product *= n    
            for idx, k in enumerate(output):
                output[idx] = int(product / nums[idx])
            return output