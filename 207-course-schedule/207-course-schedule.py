class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # A->B->C->A => false
        
        nextfirst = defaultdict(list)
        
        for next, first in prerequisites:
            nextfirst[next].append(first)
        
        visited = [0] * numCourses # 1 = visited // -1 = visited during same coursework
        
        def dfs(next):
            # base cases
            if visited[next] == 1:
                return True 
            if visited[next] == -1: #cycle
                return False
            
            visited[next] = -1 #
            for first in nextfirst[next]:
                if dfs(first) == False:
                    return False 
            visited[next] = 1
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False 
        return True 