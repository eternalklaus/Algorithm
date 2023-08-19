class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        ### binary search
        import math
        def timetakes(speed):
            time = 0
            for i, d in enumerate(dist):
                if i == len(dist)-1:
                    time += d/speed
                else:
                    time += math.ceil(d/speed)
            return time

        lo, hi = 1, 10**7 + 1 # speed
        while lo < hi: # break condition  
            middle = (lo + hi) // 2
            ### 1st consideration
            if timetakes(middle) <= hour: # fast!
                hi = middle
            else: # slow!
                ### 2nd consideration
                lo = middle + 1 
                
        return -1 if lo == 10**7 + 1 else lo
