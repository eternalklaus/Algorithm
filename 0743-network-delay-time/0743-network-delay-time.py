class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        
        graph = defaultdict(list)
        weights = [float('inf') for _ in range(n)]
        weights[k-1] = 0
        
        for i, j, w in times:
            graph[i-1].append((j-1, w))
        
        heap = [(0, k-1)]
        while heap:
            # print (heap)
            w, i = heapq.heappop(heap)
            for j, _w in graph[i]:
                weight = w + _w
                if weight < weights[j]: # 더 작은경우에만 업데이트
                    weights[j] = weight
                    heapq.heappush(heap, (weight, j))
                    
        output = max(weights)
        if output == float('inf'):
            return -1
        return output