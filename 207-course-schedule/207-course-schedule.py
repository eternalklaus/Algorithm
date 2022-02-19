class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextfirst = defaultdict(list)
        firstnext = defaultdict(list)
        
        for next, first in prerequisites:
            nextfirst[next].append(first)
            firstnext[first].append(next)
        
        # find classes don't have any prerequisites
        queue = []
        for next in range(numCourses):
            if not nextfirst.get(next):
                queue.append(next)
        
        attanded = []
        while queue:
            first = queue.pop(0)
            attanded.append(first)
            
            nexts = firstnext[first]
            for next in nexts:
                nextfirst[next].remove(first)
                if not nextfirst[next]:
                    queue.append(next)
        
        
        if len(attanded) == numCourses:
            return True 
        return False
            
            
            