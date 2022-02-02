class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter()
        tcounter = Counter(t)
        L = len(s)
        
        first, last = 0, 0
        output = ''
        
        def satisfy(counter, tcounter): # t = abcccd windows= ccckkk
            for c in tcounter:
                if counter[c] < tcounter[c]:
                    return False 
            return True 
        
        first, last = 0, 0
        for last in range(L):
            counter[s[last]] += 1
            while satisfy(counter, tcounter):
                if output == '' or len(output) > len(s[first:last+1]):
                    output = s[first:last+1]
                counter[s[first]] -= 1
                first += 1
                
        return output
            
                