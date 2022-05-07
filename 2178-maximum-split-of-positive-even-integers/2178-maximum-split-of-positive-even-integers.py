class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2: return []
        # 6 -> 2,4
        # 8 -> 2,6
        output, val = [], 2
        
        while finalSum >= val:
            output.append(val) 
            finalSum, val = finalSum-val, val+2
            
        output[-1] += finalSum
        return output 
        