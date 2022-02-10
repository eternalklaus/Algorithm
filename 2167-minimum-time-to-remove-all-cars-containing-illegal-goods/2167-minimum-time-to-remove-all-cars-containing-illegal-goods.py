class Solution:
    def minimumTime(self, s: str) -> int:
        L = len(s)
        pre, suf = [0] * L, [0] * L
        
        val = 0
        for i in range(L):
            if s[i]=='1': val += 1
            else: val -= 1
            pre[i] = val 
        
        val = 0
        for i in range(L-1, -1, -1):
            if s[i]=='1': val += 1
            else: val -= 1
            suf[i] = val 
        '''
        print (pre)
        print (suf)
        '''
        # maximum value of pre[i] + suf[i+1]
        lmax, rmax = [-L] * L, [-L] * L
        
        maxval = 0 # pre[0] # not taking any value
        for i in range(L):
            maxval = max(maxval, pre[i])
            lmax[i] = maxval
        
        maxval = 0 # suf[L-1] # not taking any value
        for i in range(L-1, -1, -1):
            maxval = max(maxval, suf[i])
            rmax[i] = maxval
        
        # print (lmax)
        # print (rmax)
        
        # get maximum value of lmax[i] + rmax[i+1]
        maxsum = 0
        maxsum = max([0, rmax[0], lmax[L-1]])
        for i in range(L-1):
            maxsum = max(maxsum, lmax[i]+rmax[i+1])
        
        # print (maxsum)
        # subtract maxsum
        
        total = 2 * s.count('1')
        return total - maxsum
            