class Solution(object):
    maxlen = 0
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def splitstr(substr): 
            if len(substr) <= self.maxlen:
                return 0
            # TODO: add another constraint in order to fasten proceeding time.
            for i in range(len(substr)):
                idx = substr.rfind(substr[i]) 
                if idx != i: # i'm not the only char 
                    substr1 = substr[:idx]
                    substr2 = substr[i:idx]
                    substr3 = substr[i+1:]
                    # print substr1, substr2, substr3
                    tmp = max(splitstr(substr1), splitstr(substr2), splitstr(substr3))
                    
                    self.maxlen = tmp if tmp > self.maxlen else self.maxlen
                    return tmp

            return len(substr) # if all chars are the only accurence, return len(substr)
        return splitstr(s)
        

sl = Solution()
print sl.lengthOfLongestSubstring("ivqpsqbpqjogwnswtimdlbxcwgeaenwokndefetwpjenwwksgwxszuwxb")