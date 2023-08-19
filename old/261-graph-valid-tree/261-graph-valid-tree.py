class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        root = [i for i in range(n)]
        def find(x):
            if root[x] != x: 
                root[x] = find(root[x])
            return root[x]
        
        
        # check "교량" node problem
        for [v1, v2] in edges:
            root1, root2 = find(v1), find(v2)
            if root1 == root2: ### insight
                return False 
            root[root1] = root2
        
        # check all nodes are connected
        if len(edges) == n-1:
            return True 
        return False 
        