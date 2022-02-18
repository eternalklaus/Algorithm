class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextfirst = defaultdict(list)
        for next, first in prerequisites:
            nextfirst[next].append(first)
        
        visited = [0] * numCourses
        
        def dfs(spot):
            if visited[spot] == -1: 
                return False 
            if visited[spot] == 1:
                return True 
            
            visited[spot] = -1 # temporarly make it un-visitable
            for first in nextfirst[spot]:
                if not dfs(first): return False
            visited[spot] = 1
            return True 
        
        for next in range(numCourses):
            if not dfs(next):
                return False
        return True