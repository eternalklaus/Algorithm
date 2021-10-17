class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        weight = [float('inf') for _ in range(n+1)]
        weight[k] = 0 # starts from k
        for [u, v, w] in times:
            graph[u].append([v, w])
        
        
        def djkstra(u):
            for [v, w] in graph[u]:
                wgt = weight[u] + w
                if wgt < weight[v]:
                    weight[v] = wgt # update shortest path
                    djkstra(v) # djkstra from v
        
        djkstra(k)
        output = max(weight[1:])
        return -1 if output == float('inf') else output