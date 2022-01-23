class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ''
        for c in s:
            if c.isalnum():
                alpha += c
        alpha = alpha.lower()
        
        li, ri = 0, len(alpha)-1
        while li < ri:
            if alpha[li]!=alpha[ri]:
                return False 
            li, ri = li+1, ri-1
        return True 