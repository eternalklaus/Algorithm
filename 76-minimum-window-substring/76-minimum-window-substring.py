class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        first, last, L = 0, 0, len(s)
        output = s+'a'
        counter = Counter(t)
        
        def increase(c):
            nonlocal counter
            if c in counter: 
                counter[c] += 1
        
        def decrease(c):
            nonlocal counter
            if c in counter: 
                counter[c] -= 1
        
        def allzeroed():
            for v in counter.values():
                if v > 0: return False 
            return True 
            
        decrease(s[0]) # initialize
        
        while True:
            # decrease window with moving first --> last
            if allzeroed():
                # update output 
                if last - first + 1< len(output):
                    output = s[first:last+1]
                # move first
                increase(s[first])
                first += 1 
                
            # increase window with moving first last -->
            else:
                last += 1
                if last >= L: break 
                decrease(s[last])
        
        if len(output) > len(s):
            return ''
        return output 