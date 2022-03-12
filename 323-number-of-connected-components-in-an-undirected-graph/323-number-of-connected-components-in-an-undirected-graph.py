class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        graph = defaultdict(list)
        
        def find(x):
            if parent[x] == x: 
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        # 앞 -> 뒤
        for [x, y] in edges:
            px, py = find(x), find(y)
            px, py = min(px, py), max(px, py)
            parent[py] = px 
        
        # 한번 스캔후 find 결과를 리턴해야 함. (parent를 바로 리턴 X)
        output = set()
        for p in parent:
            output.add(find(p))
        return len(output)