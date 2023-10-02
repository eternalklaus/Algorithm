class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        # 진입차수가 0이 아니다 = 무조건 사이클의 일부다 

        # 1. 진입차수 0인것들을 스택에 차곡차곡 넣는다
        # 2. 1과 연결된 (비-사이클) 노드들을 스택에 차곡차곡 넣는다 
        # 3. 사이클의 일부인것들의 result를 계산한다
        # 4. 스택에서 하나씩 pop하며 result를 계산한다. result = 3의 결과 + 1 
        L = len(edges)
        indegree = [0] * L
        for edge in edges:
            indegree[edge] += 1
        
        # 1. 진입차수 0인것들을 스택에 차곡차곡 넣는다
        queue = deque()
        for i in range(L):
            if indegree[i] == 0: queue.append(i)
        
        
        # 2. 1과 연결된 (비-사이클) 노드들을 스택에 차곡차곡 넣는다 
        stack = []
        while queue: # hunt zero-indegreed node 
            i = queue.popleft()
            stack.append(i)

            ipoint = edges[i]
            indegree[ipoint] -= 1
            if indegree[ipoint] == 0:
                queue.append(ipoint)
        
        # 3. 사이클의 일부인것들의 result를 계산한다
        result = [0] * L
        def calc_cycle(i):
            visit = set([])
            while i not in visit:
                visit.add(i)
                i = edges[i]
            for i in visit:
                result[i] = len(visit)
        
        stackset = set(stack)
        for i in range(L):
            if i not in stackset and not result[i]: # 싸이클의 일부이며 & 아직 계산하지 않음
                calc_cycle(i)
        
        # 4. 스택에서 하나씩 pop하며 result를 계산한다. result = 3의 결과 + 1 
        while stack:
            i = stack.pop()
            ipoint = edges[i]
            result[i] = result[ipoint] + 1

        return result

            
