class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        nums = [i for i in range(1, n+1)]
        
        def combit(idx, currentset): # combine it 
            nonlocal output
            if len(currentset) == k:
                output.append(currentset.copy())
                return
            
            if idx >= n: 
                return
            
            currentset.append(nums[idx])
            combit(idx + 1, currentset)
            currentset.pop() # pop it for next round
            combit(idx + 1, currentset)
        
        combit(0, []) 
        return output
            
            