class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # shortest processing time -> smallest index.
        from collections import defaultdict 
        import heapq
        # shortest processing time. ->  the smallest index.

        jobs = []
        for idx, task in enumerate(tasks):
            task.append(idx) # starttime, duration, idx 
        
        tasks.sort() # sort 할때 task num 이 사라지니까 같이 넣고 sort한다. 
        cpu_release_time = 0
        queue, output = [], [] 
        
        for starttime, duration, idx in tasks: 
            while cpu_release_time < starttime and queue: # do jobs until current time comes
                (__duration, __idx) = heapq.heappop(queue) ### 헷갈리지마..
                # print (__duration, __idx)
                output.append(__idx)
                cpu_release_time += __duration 
            
            cpu_release_time = max(cpu_release_time, starttime) ### 이게 진짜 중요한 구문이다
            # after cpu_release_time > duration, cannot do jobs.. just add it on the stack 
            heapq.heappush(queue, (duration, idx))
        
        while queue:
            (duration, idx) = heapq.heappop(queue)
            output.append(idx)
        return output 
                
            