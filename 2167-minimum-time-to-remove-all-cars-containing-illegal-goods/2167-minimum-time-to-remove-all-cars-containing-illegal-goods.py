class Solution:
    def minimumTime(self, s: str) -> int:
        leftmin, lrmin = 0, s.count('1')*2
        L = len(s)
        for i in range(L):
            walk = i+1
            walkandfly = leftmin + (s[i]=='1')*2 
            
            leftmin = min(walk, walkandfly)
            
            right = L - 1 - i
            
            lrmin = min(lrmin, leftmin+right)
        
        return lrmin
            