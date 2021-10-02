class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        output = defaultdict(list)
        for s in strs:
            _s = sorted(s)
            _s = ''.join(c for c in _s)
            output[_s].append(s)
        return output.values()