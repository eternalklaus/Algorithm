class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = set()
        total = len(candidates)
        
        def find(idx, current, totalsum):
            nonlocal output
            # terminate condition
            if totalsum == target:
                output.add(tuple(current.copy())) 
                return
            if totalsum > target: # we do not need to combinate the further component
                return
            if idx >= total:
                return
            
            find(idx + 1, current, totalsum)
            current.append(candidates[idx])
            find(idx, current, totalsum + candidates[idx]) # same number may be chosen an unlimited number of times
            find(idx + 1, current, totalsum + candidates[idx]) # next number is chosen
            current.pop()
        
        find(0, [], 0)
        return output