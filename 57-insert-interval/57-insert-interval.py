class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def isoverlapped(itv1, itv2):
            if itv1[0] > itv2[1]: # ...itv2...itv1... 
                return False 
            if itv2[0] > itv1[1]: # ...itv1...itv2... 
                return False
            return True
        
        def merge(i):
            nonlocal intervals
            starti = i
            interval = newInterval
            while i < len(intervals) and isoverlapped(interval, intervals[i]):
                interval = [min(interval[0], intervals[i][0]), max(interval[1], intervals[i][1])]
                i += 1
            endi = i
            intervals = intervals[:starti] + [interval] + intervals[endi:]
            
        # O(n)    
        for i in range(len(intervals)):
            if isoverlapped(newInterval, intervals[i]): # overlapped gap exist
                merge(i)
                break 
        else:
            intervals.append(newInterval)
            intervals.sort()
            
        return intervals