class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is sorted one of strs. 
        from collections import defaultdict
        outputdict = defaultdict(list)
        for s in strs:
            ss = sorted(s)
            outputdict[''.join(ss)].append(s)
        return list(outputdict.values())
            
            