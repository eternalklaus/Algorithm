class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        firstnext = defaultdict(list)
        nextfirst = Counter()
        for next, first in prerequisites:
            firstnext[first].append(next)
            nextfirst[next] += 1
        
        leaves = []
        # initialize leaves
        for c in range(numCourses):
            if nextfirst[c] == 0:
                leaves.append(c)
        
        output = []
        while leaves:
            leaf = leaves.pop(0)
            output.append(leaf)
            
            for nextleaf in firstnext[leaf]:
                nextfirst[nextleaf] -= 1
                if nextfirst[nextleaf] == 0:
                    leaves.append(nextleaf)
        
        if len(output) == numCourses:
            return output 
        return []