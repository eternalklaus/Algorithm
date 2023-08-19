class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        counter = 0 
        prevend = -5 * 10**4 - 1 
        
        for interval in intervals:
            if prevend <= interval[0]: 
                prevend = interval[1]
            else: # overlap
                prevend = min(interval[1], prevend)
                counter += 1
        return counter 