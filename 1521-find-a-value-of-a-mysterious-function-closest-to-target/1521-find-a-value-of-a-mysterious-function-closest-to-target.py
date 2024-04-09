class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ALL = 2**int(log2(10**6)+1)-1
        ### 배열 압축 
        arr = [key for key, _ in groupby(arr)]
        L = len(arr)
        sparsetable = {}
        
        # Sparse Table 계산
        for i in range(L):
            sparsetable[i, 1] = arr[i]
        
        j = 1
        while 2 ** j <= L:
            for i in range(L):
                if i + 2 ** j <= L:
                    sparsetable[i, 2 ** j] = sparsetable[i, 2 ** (j - 1)] & sparsetable[i + 2 ** (j - 1), 2 ** (j - 1)]
            j += 1
        

        def get(i, size):
            window = 2**int(log2(size))
            return sparsetable.get((i, window), ALL) & sparsetable.get((i + size - window, window), ALL)
        
        
        ### 이진 탐색 
        output = float('inf')
        for i in range(L):
            lo, hi = i, L - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                value = get(i, mid - i + 1)
                if value >= target:
                    output = min(output, abs(value - target))
                    lo = mid + 1  # 탐색 범위를 오른쪽으로 이동
                else:
                    hi = mid - 1  # 탐색 범위를 왼쪽으로 이동
            
            # 이진 탐색 후, lo가 배열 범위를 벗어나지 않고, lo 위치에서의 값을 확인하여 최솟값 업데이트
            if lo < L:
                value = get(i, lo - i + 1)
                output = min(output, abs(value - target))
            
        return output