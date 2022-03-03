class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        graph = defaultdict(list)
        
        def find(x):
            if parent[x] == x: 
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        for [x, y] in edges:
            px, py = find(x), find(y)
            px, py = min(px, py), max(px, py)
            parent[py] = px 
            
        for [x, y] in edges[::-1]:
            px, py = find(x), find(y)
            px, py = min(px, py), max(px, py)
            parent[py] = px 
        
        return len(set(parent))