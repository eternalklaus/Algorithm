class Solution(object):
    maxlen = 0
    memoization = {}
    def lengthOfLongestSubstring(self, s):
        
        """
        :type s: str
        :rtype: int
        """
        def splitstr(substr): 
            if len(substr) <= self.maxlen:
                return 0 
            if substr in self.memoization.keys(): # already calculated
                return self.memoization[substr]

            # TODO: add another constraint in order to fasten proceeding time.
            for i in range(len(substr)):
                idx = substr.rfind(substr[i]) 
                if idx != i: # i'm not the only char 
                    substr1 = substr[:idx]
                    substr2 = substr[i:idx]
                    substr3 = substr[i+1:]
                    # print substr1, substr2, substr3
                    
                    max1 = splitstr(substr1)
                    max2 = splitstr(substr2)
                    max3 = splitstr(substr3)

                    _maxlen = max(max1, max2, max3)
                    ### update memoization
                    self.memoization[substr] = _maxlen 
                    ### update maxlen
                    self.maxlen = _maxlen if _maxlen > self.maxlen else self.maxlen
                    
                    return _maxlen

            return len(substr) # if all chars are the only accurence, return len(substr)
        return splitstr(s)
        

sl = Solution()
print sl.lengthOfLongestSubstring("abcd")
# on the server, it returns 0. IDK why.