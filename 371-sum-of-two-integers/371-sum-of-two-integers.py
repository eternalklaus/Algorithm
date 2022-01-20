class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(output, carry):
            while carry:
                output, carry = output^carry, (output&carry)<<1
            return output 
        
        def sub(output, carry):
            while carry:
                output, carry = output^carry, ((~output)&carry)<<1
            return output 
            
        
        
        if abs(a) < abs(b): # abs(a) is always bigger then b!
            a, b = b, a 
            
        output, carry = abs(a), abs(b)
        
        if a<0 and b<0:
            return -add(output, carry)
        if a>=0 and b>=0:
            return add(output, carry)
        if a < 0: # abs-bigger one is minus
            return -sub(output, carry)
        if a >= 0:
            return sub(output, carry)
