class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u-1].append([v-1, w])
        dist = [float('inf')] * n 

        def dijkstra(src): # <= we can use graph inside here
            for dst, wgt in graph[src]:
                if dist[src] + wgt < dist[dst]: # update
                    dist[dst] = dist[src] + wgt
                    dijkstra(dst) # recursive call only when updated
        
        dist[k-1] = 0
        dijkstra(k-1)
        ans = max(dist)
        return ans if ans < float('inf') else -1
