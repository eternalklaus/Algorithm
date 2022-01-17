class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(interval1, interval2):
            if interval1[0] <= interval2[0] <= interval1[1]: ### range [1,4] [4,5] is also overlapped!
                return True 
            if interval2[0] <= interval1[0] <= interval2[1]:
                return True 
            return False 
        
        L = len(intervals)
        intervals.sort()
        
        for i in range(L-1):
            if overlap(intervals[i], intervals[i+1]):
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                intervals[i] = False 
        
        return [x for x in intervals if x]