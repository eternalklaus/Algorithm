class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # queries[j] = id, size
        # size보다 같거나큰 룸중에서 
        # id와의 차이가 가장적은 룸
        rooms.sort(key = lambda x:(-x[1],x[0])) # size 역순으로 정렬 4,3,2,1..
        
        queryindex = [i for i in range(len(queries))]
        queryindex.sort(key = lambda i:(-queries[i][1], queries[i][0])) # size 역순으로 정렬
        
        def put(lst, value):
            i = bisect.bisect_left(lst, value)
            if i < len(lst) and lst[i] == value:
                return 
            lst.insert(i, value)
        
        def findminabsroom(lst, value):
            if not lst: return -1
            i = bisect.bisect_left(lst, value)
            if i == 0:
                return lst[0]
            if i == len(lst):
                return lst[-1]
            if abs(lst[i-1]-value) <= abs(lst[i]-value):
                return lst[i-1]
            return lst[i]

        output = [-1] * len(queries)
        qi = ri = 0
        ridcollection = []
        for qi in queryindex:
            qid, qsize = queries[qi]
            
            while ri < len(rooms):
                rid, rsize = rooms[ri]
                if qsize > rsize: break # 취소취소 그만그만..
                put(ridcollection, rid)
                ri += 1
                
            rid = findminabsroom(ridcollection, qid)
            output[qi] = rid
        return output
         

        