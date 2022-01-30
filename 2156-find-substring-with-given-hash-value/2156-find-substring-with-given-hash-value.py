class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord('a') + 1
        
        L = len(s)
        hashval = 0
        pk = pow(power, k, modulo)
        
        for i in range(L-1, -1, -1):
            hashval = (hashval * power + val(s[i])) % modulo
            if i < L-k:
                hashval -= val(s[i+k]) * pk
                hashval %= modulo
            
            if hashval == hashValue:
                output = s[i:i+k]
        return output 