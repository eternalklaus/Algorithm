class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def getmax(t1, t2):
            if not t1 or not t2: 
                return 0
            if t1[0] == t2[0]:
                return 1 + getmax(t1[1:], t2[1:])
            else:
                l1 = getmax(t1[1:], t2) # move t1
                l2 = getmax(t1, t2[1:]) # move t2
                return max(l1, l2)
        
        return getmax(text1, text2)
                