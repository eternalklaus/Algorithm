class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        I, J = len(mat), len(mat[0])
        locs = defaultdict(list)
        
        for i in range(I):
            for j in range(J):
                locs[mat[i][j]].append((i, j))
        
        keys = list(locs.keys())
        keys.sort(reverse=True)
        
        
        _is = {} # i : max routeLength in the i # i번째 줄의 짱인거지
        _js = {} # j : max routeLength in the j
        for val in keys:
            # print (val, locs[val])
            temp_is = {}
            temp_js = {}
            for (i, j) in locs[val]:
                # 가로랑 세로 싸악~보면서 가장 큰값을 구하고 그값 + 1 해준다. 
                max_length = max(_is.get(i,0), _js.get(j,0))
                temp_is[i] = max(temp_is.get(i, 0), max_length + 1) # max_length 으로 업데이트
                temp_js[j] = max(temp_js.get(j, 0), max_length + 1) # max_length 으로 업데이트
                
            _is.update(temp_is)
            _js.update(temp_js)
#             print ('i', _is)
#             print ('j', _js)
#             print ('')
        
        # print (_is)
        # print (max(_is))
        return max(max(_is.values()), max(_js.values()))