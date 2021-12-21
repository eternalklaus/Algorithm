class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create prereqs lists
        classes = [{'BEFO':[], 'NEXT':[]} for _ in range(numCourses)]
        for [next, befo] in prerequisites:
            classes[befo]['NEXT'].append(next)
            classes[next]['BEFO'].append(befo)
        
        # select first leaves
        output = []
        stack = []
        for i in range(numCourses):
            if classes[i]['BEFO'] == []:
                output.append(i)
                stack = classes[i]['NEXT'] + stack 
        
        def canattand(i):
            for cl in classes[i]['BEFO']:
                if cl not in output: return False 
            return True 

        # select next leaves
        while stack:
            i = stack.pop()
            if canattand(i) and i not in output:
                output.append(i)
                stack = classes[i]['NEXT'] + stack 
        
        #print (output)
        if len(output) == numCourses:
            return output
        return []
            
            


