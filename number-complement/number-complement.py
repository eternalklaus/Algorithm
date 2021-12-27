class Solution:
    def findComplement(self, num: int) -> int:
        output = 0
        
        for n in bin(num)[2:]:
            output <<= 1
            if n == '1':
                output |= 0
            elif n == '0':
                output |= 1
            
        return output