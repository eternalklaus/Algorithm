class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals.append([10**4+1,10**4+1])
        def mergeable(l1, r1, l2, r2):
            return l2 <= r1
        output = []
        minleft, maxright = intervals[0]
        for left, right in intervals:
            if not mergeable(minleft, maxright, left, right):
                output.append([minleft, maxright])
                minleft, maxright = left, right
            else:
                minleft, maxright = minleft, max(maxright, right)
        return output
        