class Solution:
    def longestPalindrome(self, s: str) -> str:
        # update only when longer then longest length
        
        L = len(s)
        MAXLEN = 1
        START = 0
        for iend in range(L+1): # not include 
            # try longer odd len
            istart = iend - MAXLEN - 1
            if istart >= 0 and s[istart:iend] == s[istart:iend][::-1]:
                START = istart
                MAXLEN = MAXLEN + 1
                
            # try longer even len
            istart = iend - MAXLEN - 2
            if istart >= 0 and s[istart:iend] == s[istart:iend][::-1]:
                START = istart 
                MAXLEN = MAXLEN + 2
        
        return s[START:START+MAXLEN]
                