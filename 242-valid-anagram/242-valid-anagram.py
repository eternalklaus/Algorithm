class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Assuming that length of each string is m, n,
        # Time complexity: O(mlogm+nlogn)
        # Space complecity: O(m+n)
        '''
        s = [c for c in s]
        t = [c for c in t]
        s.sort() 
        t.sort() 
        if s==t: return True 
        return False 
        '''
        
        # Hash table
        from collections import Counter 
        counter = Counter()
        for c in s:
            counter[c] += 1
        
        if len(s)!=len(t): return False # two string should be same length
        for c in t:
            counter[c] -= 1
            if counter[c] < 0:
                return False 
        return True 