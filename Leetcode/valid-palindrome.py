class Solution(object):
    def isPalindrome(self, s):
        def strip(s):
            salpha = ""
            for c in s:
                if '0' <= c and c <= '9':
                    salpha += c 
                elif 'a' <= c and c <= 'z':
                    salpha += c 
                elif 'A' <= c and c <= 'Z':
                    salpha += c.lower()
            return salpha
        
        def ispalindrome(s):
            length = len(s)
            for i in range(length):
                print i
                if i > length - 1 - i: break 
                if s[i] != s[length - 1 - i]: return False
            
            return True
        
        return ispalindrome(strip(s))
    

s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")