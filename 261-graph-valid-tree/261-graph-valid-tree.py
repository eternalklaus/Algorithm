class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        def find(v):
            if v == parent[v]: 
                return v
            else:
                return find(parent[v])
        
        if len(edges) != n-1: return False 
        
        for [v1,v2] in edges:
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False 
            parent[p2] = p1
        return True
        
        
                