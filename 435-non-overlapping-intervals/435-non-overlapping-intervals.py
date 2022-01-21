class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        ------     ----  ---
           ------    ---
        '''
        '''
             prevend 
             |
             v
        ------
           ----
           ^
           |
          start
        '''
        
        intervals.sort()
        
        prevend = -5 * 10**4 - 1
        remove = 0
        
        
        for [start, end] in intervals:
            if start < prevend: 
                remove += 1
                prevend = min(end, prevend)
            else:
                prevend = end 
        
        return remove
                
        