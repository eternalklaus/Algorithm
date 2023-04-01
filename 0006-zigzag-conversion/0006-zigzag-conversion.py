class Solution:
    def convert(self, s: str, numRows: int) -> str:
        from collections import defaultdict
        
        rows = defaultdict(list)
        pivot, direction = 0, -1 # 1 means go to downward
        for c in s:
            rows[pivot].append(c)
            if pivot in [0, numRows-1]: 
                direction *= (-1)
            
            pivot += direction
        
        output = ''
        for i, row in rows.items():
            output += ''.join(row)
        return output 
            