class Solution:
    def subStrHash(self, s, p, m, k, hashValue):
        def val(c):
            return ord(c) - ord('a') + 1
            
        res = n = len(s)
        pk = pow(p,k,m)
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = (cur*p + val(s[i])) % m
            if i + k < n:
                cur = (cur - val(s[i+k])*pk ) % m # minus modulo also possible...!!!!!!!! 
                #print (cur)
            if cur == hashValue:
                res = i
        return s[res: res + k]