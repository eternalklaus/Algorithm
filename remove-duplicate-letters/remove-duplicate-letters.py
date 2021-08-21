class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter 
        cnt, output, input = Counter(s), '1', s

        while input:
            c, input = input[0], input[1:]
            
            # c is already exist in output
            if c in output:
                continue
            
            # c is smaller then before
            while output[-1] in input and output[-1] >= c:
                output = output[:-1]
            output += c

        return output[1:]