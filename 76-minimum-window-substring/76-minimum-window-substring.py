class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t including dupliate
        first, last, L = 0, 0, len(s)
        leftcnt, match = Counter(t), 0
        
        INTC = set(t) # interested char
        NINTC = len(INTC) # number of interested char
        
        output, outputlen = s+'$', len(s)+1
        
        # increase window size
        for last in range(L):
            c = s[last]
            leftcnt[c] -= 1
            # update match num
            if c in INTC and leftcnt[c] == 0: # newbie in zero! 
                match += 1
            
            while match == NINTC: # if all chars collected, decrease window size
                # update output 
                if last-first+1 < outputlen:
                    output = s[first:last+1]
                    outputlen = last-first+1
                # decrease window size 
                c = s[first]
                leftcnt[c] += 1
                first += 1
                # update match num
                if c in INTC and leftcnt[c] == 1: # c is no more matched char...bye.. 
                    match -= 1
        
        if outputlen > len(s):
            return ''
        return output 
                