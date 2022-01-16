class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = [] # the end time would be saved in each component of the rooms. 
        
        def allocateroom(start, end):
            nonlocal rooms
            
            # insert this range in existing room. 
            if rooms and rooms[0] <= start: # ended already before start
                heappop(rooms)
                heappush(rooms, end)
                return
            
            # allocate another room. 
            heappush(rooms, end)
            return 
        
        intervals.sort()
        for [start, end] in intervals:
            allocateroom(start, end)
        return len(rooms)
        