class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in closing:
                if stack and stack.pop() == closing[c]:
                    continue 
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True
                
            