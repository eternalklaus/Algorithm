class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        
        def getsubset(idx, current):
            output.add(tuple(current))
            
            if idx >= len(nums): return
            
            for i in range(idx, len(nums)):
                current.append(nums[i])
                getsubset(i+1, current)
                current.pop()
        
        getsubset(0, [])
        return output
                