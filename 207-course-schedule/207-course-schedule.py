class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextfirst = defaultdict(list)
        firstnext = defaultdict(list)
        
        # initialize graph
        for next, first in prerequisites:
            nextfirst[next].append(first)
            firstnext[first].append(next)
        
        # search for first visit place
        queue = []
        for next in range(numCourses):
            if not nextfirst.get(next):
                queue.append(next)
        
        # visit
        visited = []
        while queue:
            first = queue.pop(0)
            visited.append(first)
            
            nexts = firstnext[first]
            for next in nexts:
                nextfirst[next].remove(first)
                if not nextfirst[next]:
                    queue.append(next)
        
        if len(visited) == numCourses:
            return True
        return False 
        
                