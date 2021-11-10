class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def comit(comb, idx):
            if sum(comb) > target:
                return
            if sum(comb) == target:
                output.append(comb.copy()) 
                return
            
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                comit(comb, i)
                comb.pop()
        
        comit([], 0)
        return output