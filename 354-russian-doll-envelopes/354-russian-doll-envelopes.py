class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        output = [envelopes[0]]
        envelopes.sort(key=lambda x:[x[0], -x[1]])
        # [1,4], [2,9], [3,5], [4,6]
        # -> [1,4], [3,5], [4,6]
        # w 가 작다고 해서 무조건적으로 취하기 X
        # 
        # [1,4], [2,9], [3,5], [3,6], [4,7]
        
        import bisect 
        
        output = [envelopes[0][1]]
        for ww, hh in envelopes[1:]:
            idx = bisect.bisect(output, hh)
            if output[idx-1] == hh: continue 
                
            if idx == len(output):
                output.append(hh)
            else:
                output[idx] = hh 
        
        return len(output)