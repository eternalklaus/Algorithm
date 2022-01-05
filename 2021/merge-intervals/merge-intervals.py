class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        [prei, prej] = intervals[0]
        output = []
        for [i, j] in intervals:
            if i <= prej:
                prej = max(prej, j)
            else:
                output.append([prei, prej])
                prei, prej = i, j
        
        output.append([prei, prej])
        return output
