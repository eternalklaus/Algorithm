class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        I, J = len(seats), len(seats[0])
        source, sink = (-1,-1), (I,J)
        graph = defaultdict(dict)
        total_seats = 0
        
        # 0,2,4.. = source node
        for i in range(I):
            for j in range(0,J,2):
                if seats[i][j]=='#':continue
                n1 = (i,j)
                total_seats += 1
                graph[source][n1] = 1
                graph[n1][source] = 0
                for n2 in [(i,j-1), (i-1,j-1), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j-1)]: # 인접해서 앉을 수 없는 경로들 
                    ni,nj = n2
                    if 0<=ni<I and 0<=nj<J and seats[ni][nj]=='.':
                        graph[n1][n2] = 1
                        graph[n2][n1] = 0
        
        # 1,3,5.. = sink node
        for i in range(I):
            for j in range(1,J,2):
                if seats[i][j] == '#': continue
                n1 = (i,j)
                total_seats += 1
                graph[n1][sink] = 1
                graph[sink][n1] = 0
        
        # bfs로 source -> sink 경로를 탐색한다
        def bfs():
            queue, visited = deque([source]), {source}
            found = False
            parent = {source:None} ### 역사를 기록한다. 찾은 경로의 유량을 감소시켜 주기 위해서!
            while queue:
                curr = queue.popleft()
                if curr == sink:
                    found = True
                    break
                for nei in graph[curr]:
                    if nei in visited or graph[curr][nei] == 0: continue
                    queue.append(nei)
                    visited.add(nei)
                    parent[nei] = curr
            if not found: return False

            curr = sink # 자 이제 유량을 감소시켜볼까
            prev = parent[curr]
            while curr != source:
                graph[prev][curr] -= 1
                graph[curr][prev] += 1
                prev, curr = parent[prev], parent[curr]
            return True
        
        min_cut = 0
        while bfs():
            min_cut += 1
        return total_seats - min_cut
