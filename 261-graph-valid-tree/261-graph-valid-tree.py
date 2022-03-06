class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        def find(x):
            return x if parent[x] == x else find(parent[x])
        
        if len(edges) != n-1: return False ### insight
            
        for e in edges:
            x, y = find(e[0]), find(e[1]) 
            if x == y: # 두 엣지가 같은 루트를 가진다면? 
                return False
            parent[x] = y
        return True
        