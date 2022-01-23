class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time complexity: O(N^2) / Space complexity: O(n^2) including stacks of each function call 
        '''
        output, L = 0, len(s)
        def expand_palindrom(first, last):
            nonlocal output 
            
            # base cases
            if first < 0 or last >= L: 
                return 
            
            if s[first] == s[last]:
                output += 1                
                expand_palindrom(first-1, last+1)
                return 
        
        for i in range(L):
            expand_palindrom(i, i) # odd length of palindrom
            expand_palindrom(i-1, i) # even length of palindrom 
            
        return output 
        '''
        output, L = 0, len(s)
        for i in range(L):
            # odd number of palindrom
            li, ri = i, i
            while li >= 0 and ri < L and s[li] == s[ri]:
                li, ri = li-1, ri+1
                output += 1
            # even number of palindrom
            li, ri = i-1, i
            while li >= 0 and ri < L and s[li] == s[ri]:
                li, ri = li-1, ri+1
                output += 1
        return output 