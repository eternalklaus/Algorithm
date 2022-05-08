class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # second = 0 ~ 99 -> 1min 30sec -> 90sec 
        # minute = 0 ~ 99
        
        # numbers are filled from the right side 
        def getcost(m, s):
            if m > 99: ### minute exception case!!!
                return float('inf')
            
            line = str(m) + str(s).zfill(2)
            line = line.lstrip('0') ### minute exception case!!!
            
            output, current = 0, str(startAt)
            
            for c in line: 
                if current == c: # doesn't have to move
                    output += pushCost 
                else:
                    output += pushCost 
                    output += moveCost 
                    current = c # moved!
            return output 
        
        m, s = divmod(targetSeconds, 60)
        output = getcost(m, s)
        
        if s < 40 and m >= 1:
            m, s = m-1, s+60
            output = min(output, getcost(m, s))
        return output 
            