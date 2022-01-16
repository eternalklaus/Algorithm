class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = [] # the end time would be saved in each component of the rooms. 
        
        def allocateroom(start, end):
            nonlocal rooms
            # insert this range in existing room. 
            for i, room_end in enumerate(rooms):
                if start >= room_end: ### identical "=" symbol is nessasary!
                    rooms[i] = end # update end time 
                    return 
            # allocate another room. 
            rooms.append(end)
            return 
        
        intervals.sort()
        for [start, end] in intervals:
            allocateroom(start, end)
        return len(rooms)
        