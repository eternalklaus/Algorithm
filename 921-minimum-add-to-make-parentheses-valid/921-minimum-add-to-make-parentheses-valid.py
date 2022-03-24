class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        output = 0
        dept = 0
        for c in s:
            if c == '(':
                dept += 1
            elif c == ')':
                if dept > 0:
                    dept -= 1
                else: # we have no dept 
                    output += 1
        return dept + output 