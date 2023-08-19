class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # sliding window?
        # finate state machine?
        I, J = len(text1), len(text2)
        
        @cache
        def getmaxsequence(i, j):
            if i >= I or j >= J: 
                return 0
            if text1[i] == text2[j]:
                return 1 + getmaxsequence(i+1, j+1)
            else:
                return max(getmaxsequence(i, j+1), getmaxsequence(i+1, j))
        
        return getmaxsequence(0,0)
                