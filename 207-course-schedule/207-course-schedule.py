class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # circle detact 
        nextfirst = defaultdict(list)
        
        for next, first in prerequisites:
            nextfirst[next].append(first)
        
        visited = [0] * numCourses # visit: 1, visited in current coursework : -1
        
        def dfs(next):
            if visited[next] == 1:
                return True 
            if visited[next] == -1:
                return False # circle in current coursework
            
            firsts = nextfirst[next]
            visited[next] = -1 # to detect circle
            for first in firsts:
                if dfs(first) == False:
                    return False 
                
            visited[next] = 1
            return True 
        
        for next in range(numCourses):
            if not dfs(next):
                return False 
        return True
                
            