class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        m, l = 0, values[0]
        
        for i in range(1, len(values)):
            
            m = max(m, l+values[i]-i)    
            l = max(l, values[i] + i)
                
        return m