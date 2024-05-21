class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])
        
        graph = defaultdict(dict)
        total_seats = 0
        source = (-1, -1)
        sink = (R, C)
        
		# seats at even row are on the source side
		# create forward edge as well as backward edge (residual edge) with all neighbours (including odd-row seats and source)
        for r in range(R):
            for c in range(0, C, 2):
                if seats[r][c] == '#': continue
                total_seats += 1
                graph[source][r, c] = 1
                graph[r, c][source] = 0
                for nr, nc in [(r, c-1), (r-1, c-1), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c-1)]:
                    if 0 <= nr < R and 0 <= nc < C and seats[nr][nc] == '.':
                        graph[r, c][nr, nc] = 1
                        graph[nr, nc][r, c] = 0
        
		# create edges for the odd-row seats with sink
        for r in range(R):
            for c in range(1, C, 2):
                if seats[r][c] == '#': continue
                total_seats += 1
                graph[r, c][sink] = 1
                graph[sink][r, c] = 0
    
		# bfs to find a path from source to sink. if found, augmenting the edges along the path
		# here all the edge capacity is max 1, therefore, once a path is found, we can include max network flow by 1
        def bfs(node, graph):
            visited = {node}
            queue = deque([node])
            parent = {node: None}
            
            found = False
            while queue:
                curr = queue.popleft()
                if curr == (R, C):
                    found = True
                    break
                for nei in graph[curr]:
                    if nei in visited or graph[curr][nei] == 0: continue
                    visited.add(nei)
                    queue.append(nei)
                    parent[nei] = curr
            
            if not found: return False
            curr = (R, C)
            prev = parent[curr]
            while prev:               # this is the augmenting part, decrease forward edge by 1, and increase backwared edge by 1
                graph[prev][curr] -= 1
                graph[curr][prev] += 1
                curr, prev = prev, parent[prev]
            return True
        
		# max flow equals min cut, equals maximum bipartite matching, meaning at least this amount of seats can't be used.
        min_cut = 0
        while bfs(source, graph):
            min_cut += 1

        return total_seats - min_cut