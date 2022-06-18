class Solution:
    def isPalindrome(self, x: int) -> bool:
        x =  str(x)
        li, ri = 0, len(x)-1
        while li < ri:
            if not x[li] == x[ri]:
                return False 
            li += 1
            ri -= 1
        return True