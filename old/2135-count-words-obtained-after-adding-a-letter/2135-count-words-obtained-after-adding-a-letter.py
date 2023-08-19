class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        from collections import Counter 

        startbits, targetbits = Counter(), Counter()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        for sw in startWords:
            wordbit = 0
            for c in sw:
                wordbit |= 1 << (ord(c) - ord('a'))
            startbits[wordbit] += 1
        
        for tw in targetWords:
            wordbit = 0
            for c in tw:
                wordbit |= 1 << (ord(c) - ord('a'))
            targetbits[wordbit] += 1
        
        # print (targetbits)
        output = 0
        for sb in startbits:
            for c in alphabet:
                tb = sb | (1 << ord(c) - ord('a'))
                if tb == sb: # bit does not exist in the tb 
                    continue 
                output += targetbits[tb]
                targetbits[tb] = 0 
            '''
            for tb in targetbits:
                xorb = sb ^ tb
                if sb < tb and xorb & -xorb == xorb:
                    # print (bin(sb), bin(tb), bin(xorb))
                    output += targetbits[tb]
                    targetbits[tb] = 0 # clean it out
            '''
        return output 
            