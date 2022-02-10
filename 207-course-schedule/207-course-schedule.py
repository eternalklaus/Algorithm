class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        firstnext = defaultdict(list)
        nextfirst = defaultdict(list)

        for [next, first] in prerequisites:
            firstnext[first].append(next)
            nextfirst[next].append(first)
        
        # initialize queue
        queue = []
        for next in range(numCourses): ###<-!!!
            if not nextfirst[next]: # does not have any prerequist subjects
                queue.append(next) 
        # print (queue)

        # conquar subjects from one by one 
        count = 0
        while queue:
            first = queue.pop(0)
            count += 1
            for next in firstnext[first]:
                nextfirst[next].remove(first) # attanded [first], so remove it from prerequisites
                if not nextfirst[next]: # does not have any preerquist subject. attandable
                    queue.append(next)
        
        return count == numCourses