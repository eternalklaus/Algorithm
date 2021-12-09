class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # one can move onle "arr[i]" step forware/backward
        visited = [False for _ in range(len(arr))]
        output = False 
        def visit(i): # visit i and visit another location
            # Jump out of array
            if i < 0 or i >= len(arr): return 
            
            # Already visited
            if visited[i] == True: return 
            
            # Accomplished goal 
            if arr[i] == 0:
                nonlocal output 
                output = True 
                return 
            
            visited[i] = True # now we visit here
            visit(i - arr[i])
            visit(i + arr[i])
        
        
        visit(start)
        return output 
            