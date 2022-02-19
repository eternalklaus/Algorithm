class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        firstnext = defaultdict(list)
        nextfirst = defaultdict(list)
        
        # initialize
        for next, first in prerequisites:
            firstnext[first].append(next)
            nextfirst[next].append(first)
            
        # queue initialize
        queue = []
        for next in range(numCourses):
            if not nextfirst.get(next):
                queue.append(next)
        
        # pop queue
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