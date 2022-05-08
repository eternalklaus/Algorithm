class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort() # x would be acsending order 
        INF = float('inf')
        
        xy = defaultdict(list)
        for x,y in points:
            xy[x].append(y)
        
        output = INF
        for x2 in xy: ###
            for x1 in xy:
                if x2 <= x1: break
                ycommon = [y for y in xy[x1] if y in xy[x2]] # 공통 y만 구한다
                ycommon.sort()
                dy = INF
                for y1, y2 in zip(ycommon, ycommon[1:]):
                    dy = min(dy, y2-y1)
                output = min((x2-x1) * dy, output)
        
        if output < INF: return output 
        return 0