class Solution(object):
    def validPalindrome(self, s):
        def ispalindrome(_s):
            return _s == _s[::-1]

        length = len(s)
        ri = len(s) - 1
        li = 0
        while li < ri:
            if s[li] == s[ri]:
                li += 1
                ri -= 1
            else:
                ret1 = ispalindrome(s[li:ri]) # strip ri
                ret2 = ispalindrome(s[li + 1:ri + 1]) # strip li
                return ret1 | ret2
        return True


sl = Solution()
print sl.validPalindrome("abca")