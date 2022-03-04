class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        import math
        degrees, count, output = [], 0, 0
        
        for x, y in points:
            if [x, y] == location: ### include this point regardless of the degree. 
                count += 1
                continue 
            x, y = x-location[0], y-location[1]
            degree = math.atan2(y, x) / (2 * math.pi) * 360  ### 
            if degree < 0: 
                degree += 360 
            degrees.append(degree)
        output = max(output, count) ### 아래 for loop가 돌지 않을 것을 대비하여 output을 최초에 업데이트해 둠 
        
        degrees.sort()
        degrees += [360+d for d in degrees] ### # 환형 자료구조에서 어떻게 동일한 값은 1번만 포함되도록 할 것인가? 
        li = 0
        for ri in range(len(degrees)): # ri = enddegree
            while degrees[ri] - degrees[li] > angle: # li = startdegree ###!
                li += 1
                count -= 1
            count += 1
            output =  max(output, count)
        return output 
            
                