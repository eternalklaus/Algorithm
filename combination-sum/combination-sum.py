class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = set()
        total = len(candidates)
        
        def find(idx, current):
            nonlocal output
            # terminate condition
            if sum(current) == target:
                output.add(tuple(current.copy())) 
                return
            if sum(current) > target: # we do not need to combinate the further component
                return
            if idx >= total: 
                return
            
            find(idx + 1, current)
            current.append(candidates[idx])
            find(idx, current) # same number may be chosen an unlimited number of times
            find(idx + 1, current) # next number is chosen
            current.pop()
        
        find(0, [])
        return output