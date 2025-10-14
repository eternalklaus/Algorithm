class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        '''
        하나의 사이클이 3스페이스짜리임
        태스크를 하나씩 돌면서 인덱스를 저장
        현재 인덱스 curr_idx - 테스크의 인덱스 
        '''
        last_idx = defaultdict(lambda: -space-1)
        curr_idx = 0
        for t in tasks:
            if curr_idx - last_idx[t] >= space + 1:
                last_idx[t] = curr_idx
            else:
                last_idx[t] = curr_idx + (space + 1 - (curr_idx - last_idx[t]))
            curr_idx = last_idx[t] + 1
            
        return curr_idx

