class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # join 
        # timestamp, a, b 
        parent = [i for i in range(n)]
        logs.sort()
        def find(x):
            if parent[x] == x: return x 
            parent[x] = find(parent[x]) # path comprehension 
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            px, py = min(px, py), max(px, py)
            parent[py] = px # x팀의 수장(px)과 y팀의 수장(py)을 교량으로 연결 
            #print (f'queen: {px}, {py}')
            # find(y) # 팀 모두 업데이트 한번 싹~ 1,2,3,4 / 5,6,7,8 일때 union(3, 8)한다면 4에 대한 union은 안됨. 
            
            
        for timestamp, a, b in logs:
            union(a, b)
            for x in range(n): # 정방향으로 한번만 해줘도 될것같은데? 왜냐면 항상 방향성이 작은수<-큰수 이니까 작은것부터 정리를 해나가보는거지. 
                find(x)
            #print (timestamp, parent)
            
            if len(set(parent)) == 1:
                return timestamp
        return -1

