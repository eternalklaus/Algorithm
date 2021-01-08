class Solution(object):
    def num_minusvalue(self, mystr, lastidx):
        if lastidx < 0:
            return 0

        backspace = self.num_backspace(mystr, lastidx)
        if backspace == 0:
            return 1
        else: 
            return backspace * 2

    def num_backspace(self, mystr, lastidx):
        backspace = 0
        while lastidx - backspace >= 0:
            if mystr[lastidx - backspace] is not '#': break
            backspace += 1
        print 'backspace = %d' % backspace
        return backspace

    def backspaceCompare(self, S, T):
    
        s = len(S) - 1
        t = len(T) - 1
        
        while True:

            print 's=%d t=%d' % (s,t)
            if s < 0 and t < 0: return True
            if s >= 0 and t >= 0:
                if S[s] != T[t]: return False
            
            s_minusvalue = self.num_minusvalue(S, s)
            s = s - s_minusvalue
            
            t_minusvalue = self.num_minusvalue(T, t)
            t = t - t_minusvalue
            print s_minusvalue, t_minusvalue

sl = Solution()
print sl.backspaceCompare("ab#c", "ad#c")


