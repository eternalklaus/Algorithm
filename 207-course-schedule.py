class Solution(object):
    def isCyclic(self, classnum, visited):
        
        if self.prereqes[classnum] == []: 
            return False 
        if classnum in visited: # Cycle detected
            return True 
        
        visited.append(classnum)

        ### "for loop" + "recursive call"
        for c in self.prereqes[classnum]:
            result = self.isCyclic(c, visited)
            if result == True:
                return True
        
        self.prereqes[classnum] = [] # This is all passed(noncyclic) childs. So equal to the effect of []
        return False


    def canFinish(self, numCourses, prerequisites):
        ### Init prereqes
        self.prereqes = {}
        for i in xrange(numCourses):
            self.prereqes[i] = []
        
        ### Set prereqes 
        for p in prerequisites:
            nextclass = p[0]
            prevclass = p[1]
            self.prereqes[nextclass].append(prevclass)
        
        ### Check cycle 
        result = True
        for i in xrange(numCourses):
            is_cyclic = self.isCyclic(i, [])
            if is_cyclic == True:
                result = False 
                break
                 
        return result