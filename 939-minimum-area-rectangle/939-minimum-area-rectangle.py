class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        xy = defaultdict(list)
        for x,y in points:
            xy[x].append(y)
        
        output = float('inf')
        for x2 in xy:
            for x1 in xy:
                if x1 >= x2: break  ### 순서를 바꿔서 브래이크 제동을 걸어줬다
                if x2-x1 > output: continue 
                ys = [y for y in xy[x1] if y in xy[x2]]
                if len(ys) <= 1: continue
                
                # get most mininmum diff between all element 
                ys.sort()
                dy = float('inf')
                # print (x1,x2)
                # print (ys)
                for y1, y2 in zip(ys, ys[1:]):
                    dy = min(dy, y2-y1)
                    # print (f'dy={dy}')
                output = min(output, (x2-x1)*dy)
                # print (f'output={output}')
        return output if output != float('inf') else 0
                