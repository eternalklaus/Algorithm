class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # search from arbitrary root(=0)
        queue, visited = [0], set()
        while queue:
            node = queue.pop(0)
            if node in visited: return False 
            visited.add(node)
            
            nextnodes = graph[node]
            # preprocessing
            for nn in nextnodes: # remove connection to node...
                graph[nn].remove(node)
            queue += nextnodes
            # print (queue)
                
        # print ('a')
        return len(visited) == n