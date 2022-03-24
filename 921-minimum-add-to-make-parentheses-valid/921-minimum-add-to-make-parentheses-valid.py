class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # shorten paranthesis string by compressing it 
        stack = []
        for c in s:
            if c == '(': 
                stack.append(c)
            else:
                if stack and stack[-1] == '(': 
                    stack.pop() # can complete one pair
                else: 
                    stack.append(c) # append )
        # result = "))((("
        return len(stack)
        