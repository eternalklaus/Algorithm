class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prergraph = [[] for i in range(numCourses)]
        nextgraph = [[] for i in range(numCourses)]
        for [c2, c1] in prerequisites:
            prergraph[c2].append(c1)
            nextgraph[c1].append(c2)
        
        stack = []
        # find the first leaf
        for i, prereq in enumerate(prergraph):
            if prereq == []:
                stack.append(i)
        
        
        # drop leaves 
        ###output = set() # set is better since common nexti can be pushed into output at the same time
        output = []
        while stack:
            leaf = stack.pop()
            if prergraph[leaf] == [] and leaf not in output: 
                output.append(leaf) 
                for branch in nextgraph[leaf]:
                    prergraph[branch].remove(leaf) # drop this leaf from all connected branches
                stack = nextgraph[leaf] + stack # connected branches has posibility of being leaf!

        if len(output) == numCourses:
            return output 
        return []
