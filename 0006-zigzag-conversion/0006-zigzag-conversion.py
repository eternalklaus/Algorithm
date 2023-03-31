class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # chars per pair = numRows * 2 - 2
        # every pair[0] in the same row
        # every pair[1], pair[-1] in the same row
        # every pair[2], pair[-2] in the same row
        # ... 
        # every pair[numRows - 1] in the same row
        
        if numRows == 1:
            return s

        rowLen = numRows * 2 - 2
        L, output = len(s), ''
        
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                row = s[i::rowLen]
                output += ''.join(row)
                
            else:
                li = i
                ri = rowLen - i
                row1 = s[li::rowLen] + '_'
                row2 = s[ri::rowLen] + '_'
                row = [c1 + c2 for c1, c2 in zip(row1, row2)]
                
                output += ''.join(row).rstrip('_')
        
        return output
            
            
        