class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(xy):
            x, y = list(map(find, xy))
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        parent, rank = [i for i in range(n)], [0] * n
        list(map(union, edges))
        return len({find(x) for x in parent})

        map(union, edges)
        return len({find(x) for x in parent})