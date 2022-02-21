class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        
        def conquer(node):
            if node in visited:
                return
            else:
                visited.add(node)
                for nn in graph[node]:
                    conquer(nn)
                return 
        
        output = 0
        for node in range(n):
            if node not in visited:
                output += 1
                conquer(node)
        return output 