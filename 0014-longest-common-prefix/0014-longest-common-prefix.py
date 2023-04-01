class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs.pop(0) # if len(common)==1, return common
        for s in strs: 
            new_common = ''
            for c1, c2 in zip(common, s): # if len(s) == 0, return ''
                if c1 == c2: new_common += c1
                else: break 
            common = new_common
        return common