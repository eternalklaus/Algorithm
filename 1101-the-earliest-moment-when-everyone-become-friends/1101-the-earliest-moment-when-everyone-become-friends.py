class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # [step1] root 초기회
        parent = [i for i in range(n)]
        logs.sort()
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            px, py = min(px, py), max(px, py)
            parent[py] = parent[px] # 두 세력간에 가교를 잇는다
        
        for time, x, y in logs:
            # [step2] 두 세력장 사이에 가교를 잇는다
            union(x, y)
            # [step3] 두 세력의 구성원들에게 업데이트를 전파한다
            for i in range(n):
                find(i)
            if len(set(parent)) == 1:
                return time
        return -1