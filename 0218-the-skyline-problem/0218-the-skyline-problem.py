class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        
        # write any changes : appear(start), disappear(end)
        changes = []
        for start, end, height in buildings:
            changes.append((start, end, height))
            changes.append((end, end+1, 0))
        changes.sort()
        
        heap = []
        output_y = [-1] # 이건 나중에 빼줄것이다
        output_x = [-1]
        for start, end, height in changes:
            heapq.heappush(heap, (-height, start, end))
            
            while heap:
                h, s, e = heapq.heappop(heap)
                h = -h # correction
                
                if start < e: # 높이의 유효성이 현재(start)까지 지속되고있다면 
                    heapq.heappush(heap, (-h, s, e))
                    if output_x[-1] == start: # 이전x와 같다면? 이전꺼(높이0)은 잊자...
                        output_x.pop()
                        output_y.pop()
                    if output_y[-1] != h: # 이전높이와 다를때에만 기록하는데...
                        output_y.append(h)
                        output_x.append(start)
                    
                    break 
        
        return list(zip(output_x, output_y))[1:]