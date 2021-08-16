class Solution:
    def networkDelayTime(self, times, N, K):
        from collections import defaultdict 
        import heapq

        weight = defaultdict(list)
        for src,dst,wgt in times:
            weight[src - 1].append([dst - 1,wgt])
        
        heap = [[0, K - 1]]
        dist = [float('inf') for _ in range(N)]

        while heap:
            srcwgt, src = heappop(heap)
            if dist[src] > srcwgt:
                dist[src] = srcwgt 
                for dst, dstwgt in weight[src]:
                    heap.append([srcwgt+dstwgt, dst])

        print (dist)
        return -1 if max(dist) == float('inf') else max(dist)
