class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        def popstr():
            nonlocal stack 
            output = ''
            while True:
                c = stack.pop()
                if c == '[':
                    break 
                output = c + output 

            num, digit = 0, 1
            while stack and stack[-1].isnumeric():
                num += digit * int(stack.pop())
                digit *= 10
            
            if num: return num * output 
            else: return output 

        for c in s:
            if c == ']': 
                s = popstr()
                stack.append(s)
            else:
                stack.append(c)
            
        return ''.join(stack)