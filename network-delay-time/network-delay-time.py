class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        delay = {}

        for (u, v, w) in times:
            graph[u].append((w, v))
        
        # conquar from the shortest one
        queue = [(0, k)]
        while queue:
            (wgt, dst) = heappop(queue)
            if dst not in delay:
                delay[dst] = wgt 
                for (w, v) in graph[dst]:
                    # queue.append((w+wgt, v))
                    heappush(queue, (w+wgt, v))
        
        # print (delay)
        # print (max(delay.values()))
        return -1 if len(delay) != n else max(delay.values())
