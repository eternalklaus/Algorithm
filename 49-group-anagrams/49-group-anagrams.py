class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is sorted one of strs. 
        from collections import defaultdict
        def sortstr(s):
            result = [c for c in s]
            result.sort()
            return ''.join(result)
            
        outputdict = defaultdict(list)
        for s in strs:
            ssort = sortstr(s)
            outputdict[ssort].append(s)
        '''
        print (list(outputdict.keys()))
        print (list(outputdict.values()))
        '''
        return list(outputdict.values())
            
            