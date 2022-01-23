class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        overlap_start, overlap_end = 0, len(intervals)
        
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]: # before the overlapping range
                overlap_start = i + 1
                overlap_end = i
            elif interval[0] > newInterval[1]: # passed the overlapping range
                overlap_end = i - 1
                break 
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                overlap_end = i 
        
        return intervals[:overlap_start] + [newInterval] + intervals[overlap_end+1:]
                
