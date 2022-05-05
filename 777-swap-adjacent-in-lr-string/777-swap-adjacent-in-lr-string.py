class Solution:
    def canTransform(self, start: str, end: str) -> bool:
            
        if len(start) != len(end): return False 
        N = len(start)
        si, ei = 0, 0
        
        def encrease(ei):
            while ei < N and end[ei] == 'X':
                ei += 1
            return ei
        
        while si < N:
            ch = start[si]
            if ch == 'L':
                ei = encrease(ei)
                if ei >= N or end[ei] != 'L' or si < ei:
                    return False
                si += 1
                ei += 1
                continue 
            
            elif ch == 'R':
                ei = encrease(ei)
                if ei >= N or end[ei] != 'R' or si > ei:
                    return False
                si += 1
                ei += 1
                continue
            
            si += 1
        
        ei = encrease(ei)
        return ei == si
            
        