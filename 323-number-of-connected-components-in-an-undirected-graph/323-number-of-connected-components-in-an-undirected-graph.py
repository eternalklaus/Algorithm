class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for [src,dst] in edges: # undirectional
            graph[src].append(dst)
            graph[dst].append(src)
        
        visited = set()
        def visit(point):
            if point in visited:
                return False 
            
            visited.add(point)
            for np in graph[point]:
                visit(np)
            return True
        
        output = 0
        for point in range(n):
            if visit(point): output += 1
        return output 
            
        
        