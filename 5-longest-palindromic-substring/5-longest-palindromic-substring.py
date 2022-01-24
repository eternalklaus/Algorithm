class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        def getlongestpal(idx):
            li, ri = idx, idx 
            str1, str2 = s[idx], s[idx]
            while li >= 0 and ri < L and s[li] == s[ri]:
                str1 = s[li:ri+1]
                li -= 1
                ri += 1
            
            li, ri = idx-1, idx 
            while li >= 0 and ri < L and s[li] == s[ri]:
                str2 = s[li:ri+1]
                li -= 1
                ri += 1
            
            if len(str1) > len(str2):
                return str1 
            return str2
                
        
        output = ''
        for i in range(L):
            palindrom = getlongestpal(i)
            if len(palindrom) > len(output):
                output = palindrom
        return output 