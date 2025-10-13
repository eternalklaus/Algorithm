class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        a1b1
        ㄴ a 1 
              ㄴ b
              ㄴ B
        ㄴ A 1
        '''
        def perm(i, curr):
            if i == len(s):
                output.append(curr)
                return 
            if '0' <= s[i] <= '9':
                perm(i+1, curr + s[i])
                return
            else:
                perm(i+1, curr + s[i].upper())
                perm(i+1, curr + s[i].lower())
                return
        
        output = []
        perm(0, '')
        return output