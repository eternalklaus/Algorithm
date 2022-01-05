class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s): # if bigger then previous list, eat them
            remain = s[i+1:]
            if c in stack: continue
            while stack and stack[-1] >= c: # c is stronger
                if stack[-1] in remain: 
                    stack.pop()
                else:
                    break
            stack.append(c)
            # stronger(smaller) alaphabet eats previous weaker chars
            # if previous weaker char is duplicated, cannot avoid attack
            # else, can avoid attack
        return ''.join(stack)
            
            