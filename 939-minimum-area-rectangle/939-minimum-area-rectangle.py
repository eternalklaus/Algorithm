class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xy = defaultdict(list)
        for x, y in points:
            xy[x].append(y)
        
        output = float('inf')
        
        xlist = sorted(xy)
        for ri in range(len(xlist)):
            for li in range(ri-1, -1, -1):
                x1, x2 = xlist[li], xlist[ri]
                dx = x2 - x1
                if dx >= output: # 가로길이에서 이미 넘어버림
                    break 
                    
                # filter common y
                common_y = [y for y in xy[x1] if y in xy[x2]]
                common_y.sort() 
                
                # pick minimum dy  
                dy = float('inf')
                for y1, y2 in zip(common_y, common_y[1:]):
                    dy = min(y2-y1, dy)
                output = min(output, dy*dx)
        return 0 if output == float('inf') else output
                
                