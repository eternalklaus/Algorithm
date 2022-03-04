class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        import math
        
        degrees, extra = [], 0, ### extra로 선언한다
        xx, yy = location
        for x, y in points:
            if [x, y] == location: ### include this point regardless of the degree. 
                extra += 1
                continue 
            degree = math.atan2(y-yy, x-xx) / (2 * math.pi) * 360  ### 
            degrees.append(degree % 360) ### correct minus value 
        
        degrees.sort()
        
        degrees += [360+d for d in degrees] ### # 환형 자료구조에서 어떻게 동일한 값은 1번만 포함되도록 할 것인가? 
        li = output = 0 ### count 도 사실 필요없지, li, ri가 주어져 있는데. 
        for ri in range(len(degrees)): # ri = enddegree
            while degrees[ri] - degrees[li] > angle: # li = startdegree ###!
                li += 1
            output =  max(output, ri - li + 1)
        return output + extra
            
                