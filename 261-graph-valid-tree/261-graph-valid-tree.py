class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        ###???
        if n == 1: return True 
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # gather leaf
        queue = []
        for i in range(n):
            if i not in graph: return False # i isn't connected at mainstream
            if len(graph[i]) == 1: 
                queue.append(i)
        
        # drop leaf one by one
        root = False
        while queue:
            leaf = queue.pop(0)
            nextleaves = graph[leaf]
            for nl in nextleaves:
                graph[nl].remove(leaf)
                if len(graph[nl]) == 0: # we found root! 루트는 하나야 
                    if root: return False # root is already written
                    root = nl
                if len(graph[nl]) == 1:
                    queue.append(nl)
            
            del graph[leaf] # remove the trace of leaf.. 
            
        
        if not graph: # if not all nodes' been toured, return False
            return True
        return False 