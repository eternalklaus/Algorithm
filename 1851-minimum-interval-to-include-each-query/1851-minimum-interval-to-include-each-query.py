class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries2 = sorted(queries)
        intervals.sort()
        
        heap, output = [], {} # minheap, (width, expires_at)
        i = 0
        for q in queries2: 
            while i < len(intervals) and intervals[i][0] <= q:
                a,b = intervals[i][0], intervals[i][1]
                heappush(heap, (b-a+1, b))
                i += 1
            # take the smallest width from heap 
            smallest_width = -1
            while heap:
                width, expires_at = heappop(heap)
                if expires_at >= q: # q를 포용하는 범위
                    smallest_width = width
                    heappush(heap, (width, expires_at))
                    break
            output[q] = smallest_width
        return [output[_] for _ in queries] # 원본 순서
        