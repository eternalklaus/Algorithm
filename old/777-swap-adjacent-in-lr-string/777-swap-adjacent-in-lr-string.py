class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False 
        if start.replace('X','') != end.replace('X',''):
            return False 
        n = len(start)
        sL = [i for i in range(n) if start[i] == 'L']
        sR = [i for i in range(n) if start[i] == 'R']
        eL = [i for i in range(n) if end[i] == 'L']
        eR = [i for i in range(n) if end[i] == 'R']
        
        for si, ei in zip(sL, eL):
            if si < ei: return False
        for si, ei in zip(sR, eR):
            if si > ei: return False
        return True