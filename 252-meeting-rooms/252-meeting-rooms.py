class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # if one of the meeting is overlaped, return False
        intervals.sort()
        before_end = -1
        for [start, end] in intervals:
            if start < before_end: 
                return False 
            before_end = end
        return True 