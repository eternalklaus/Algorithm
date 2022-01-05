class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = set()

        def getperm(current, exist):
            nonlocal output 
            
            if len(current) == len(nums): 
                output.add(tuple(current))
            
            for i, e in enumerate(exist):
                if exist[i] == 0: # not exist in current! let's pick it
                    current.append(nums[i])
                    exist[i] = 1
                    getperm(current, exist)
                    exist[i] = 0
                    current.pop()

        exist = [0 for _ in range(len(nums))]
        getperm([], exist)    
        return output