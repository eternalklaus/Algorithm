class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # 오른쪽으로만 점프할 수 있음 
        # odd number jump: 나보다 큰곳들 중 최대한 작은곳으로
        # even number jump: 나보다 작은곳들 중 최대한 큰곳으로
        # 오른쪽 끝까지 갈수잇다면 good
        ascending = sorted([(n, i) for i, n in enumerate(arr)])
        descending = sorted([(-n, i) for i, n in enumerate(arr)]) # i는 작아야좋고 n은 커야좋고
        
        next_high = [-1] * len(arr)
        next_low = [-1] * len(arr)
        stack = []
        for n, i in ascending:
            # 나보다 왼쪽인것들? 근데 스택에잇다? (나보다작다) => 다 나와서 나를 바라봐줘
            while stack and stack[-1] < i:
                next_high[stack.pop()] = i
            stack.append(i)
        
        for n, i in descending:
            while stack and stack[-1] < i:
                next_low[stack.pop()] = i
            stack.append(i)
        
        result = [False] * len(arr)
        result[-1] = True
        ODD, EVEN = 0, 1
        def search(i, mode):
            if i == len(arr)-1:
                return True
            if i == -1:
                return False
            if mode == ODD:
                return search(next_high[i], EVEN)
            elif mode == EVEN:
                return search(next_low[i], ODD)
        
        output = 0
        for i in range(len(arr)):
            output += search(i, ODD)
        return output
            
