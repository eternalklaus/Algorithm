class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def splitstr(substr): 
            for i in range(len(substr)):
                idx = substr.rfind(substr[i]) 
                if idx != i: # i'm not the only char 
                    # print idx
                    substr1 = substr[:idx]
                    substr2 = substr[i:idx]
                    substr3 = substr[i+1:]
                    # print substr1, substr2, substr3
                    return max(splitstr(substr1), splitstr(substr2), splitstr(substr3))

            return len(substr) # if all chars are the only accurence, return len(substr)
        return splitstr(s)

sl = Solution()
print sl.lengthOfLongestSubstring("xpxbcivfbzjamznjfjxjgholjllyhwignfhpnexqdisshfbnp")