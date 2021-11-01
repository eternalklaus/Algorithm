class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        weight = defaultdict(list)
        delay = [float('inf') for _ in range(n+1)]
        delay[k] = 0

        for (u, v, w) in times:
            weight[u].append((w, v))
        
        def queuedist(src):
            wgt = delay[src]
            for (w, v) in weight[src]:
                if wgt + w < delay[v]: # found shorter path
                    delay[v] = wgt + w 
                    queuedist(v)
        
        queuedist(k)
        # print (delay)
        output = max(delay[1:])
        
        if output == float('inf'): return -1
        return output

        