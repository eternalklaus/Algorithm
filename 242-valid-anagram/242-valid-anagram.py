class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [c for c in s]
        t = [c for c in t]
        s.sort() 
        t.sort() 
        if s==t: return True 
        return False 