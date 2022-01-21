class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        def insertroom(interval):
            nonlocal rooms
            for i, endtime in enumerate(rooms):
                if endtime <= interval[0]: # room is already empty
                    rooms[i] = interval[1]
                    return True 
            return False 
                
        intervals.sort()
        for interval in intervals:
            if insertroom(interval) == False:
                rooms.append(interval[1])
        
        return len(rooms)