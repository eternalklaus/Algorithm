class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 전략: (끝시간, 방번호)를 큐에 넣는다
        # 새 미팅이 들어온다 -> 미팅 시작 시간보다 전에 끝난 미팅의 방 정리
        # 정리후, len(q) < n: 바로 사용한다 -> 어떤 방을 사용할 것인가? emptyrooms 셋 참고
        # len(q) == n: q[0]방이 끝난 후 바로 사용한다
        q = []
        emptyrooms = [i for i in range(n)]
        usecnt = Counter()
        meetings.sort()
        def clean_rooms(q, t):
            while q:
                t2, roomno = q[0]
                if t2 <= t: 
                    heapq.heappop(q)
                    heapq.heappush(emptyrooms, roomno)
                else:
                    return

        for t1, t2 in meetings:
            clean_rooms(q, t1) # t1전에 끝난 미팅들 방 정리
            if emptyrooms:
                roomno = heapq.heappop(emptyrooms)
                heapq.heappush(q, (t2, roomno))
                usecnt[roomno] += 1
            
            else: # 모든 방이 사용중
                (t, roomno) = heapq.heappop(q) # 제일 먼저 끝나는 방
                diff = t - t1
                
                heapq.heappush(q, (t2 + diff, roomno)) # 끝나는 시간 갱신
                usecnt[roomno] += 1

        return usecnt.most_common(1)[0][0]