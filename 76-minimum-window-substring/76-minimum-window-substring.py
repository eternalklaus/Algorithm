class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        first, last, L = 0, 0, len(s)
        output = s+'$'
        counter = Counter(t)
        keys = counter.keys()
        
        # O(1) 
        def allzeroed():
            for c in keys: ### be careful not "c in t"
                if counter[c] > 0: return False 
            return True 
            
        counter[s[0]] -= 1 # initialize!!!
        while True:
            # decrease window with moving [first --> last]
            if allzeroed():
                if last - first + 1< len(output): # update output 
                    output = s[first:last+1]
                # move first
                counter[s[first]] += 1
                first += 1 
                
            # increase window with moving [first last -->]
            else:
                last += 1
                if last >= L: break 
                counter[s[last]] -= 1
        
        if len(output) > len(s):
            return ''
        return output 