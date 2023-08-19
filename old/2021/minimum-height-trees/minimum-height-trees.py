class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #// weird tree only consist of leaves
        if n <= 2:
            return [x for x in range(n)]
        
        #// make connected graph
        connected = [[] for _ in range(n)]
        for [i, j] in edges:
            connected[i].append(j)
            connected[j].append(i)
        
        #// find last leaves
        leaves = [] #// only contains the final leaves (has only one node) 
        for v in range(n):
            if len(connected[v]) == 1: #// leaf
                connected[v]
                leaves.append(v)
        leaves.append(-1)
        
        total = n
        while leaves:
            leaf = leaves.pop(0)
            if leaf == -1: #// end of this level
                if total <= 2:
                    return leaves
                else:
                    leaves.append(-1)
                    continue
            
            #// get branch that has the leaf
            print (connected[leaf])
            branch = connected[leaf][0]
            
            #// drop the leaf
            total -= 1
            connected[leaf].remove(branch)
            connected[branch].remove(leaf)
            
            #// if this branch was also a leaf? append leaves
            if len(connected[branch]) == 1:
                leaves.append(branch)
            
        

