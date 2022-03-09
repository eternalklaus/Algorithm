class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        L = len(rooms)
        visited, currentkeys = set([0]), []
        
        # TC : L * n
        currentkeys += rooms[0]
        while currentkeys:
            r = currentkeys.pop(0)
            
            if r in visited: continue # O(1)
            
            visited.add(r)
            currentkeys += rooms[r]
            
        
        return len(visited) == L