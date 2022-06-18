class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # shortest processing time -> smallest index.
        from collections import defaultdict 
        import heapq
        jobs = defaultdict(list)
        
        for tasknum, task in enumerate(tasks):
            t_start, t_duration = task 
            jobs[t_start].append(tasknum)
        
        starttimes = list(jobs.keys())
        starttimes.sort()
        
        candojob, queue, output = 0, [], []
        
        for starttime in starttimes:
            while candojob < starttime and queue: # 이전시간대에 처리가능했던 것들을 몰아서 처리한다
                (t_duration, tasknum) = heappop(queue)
                candojob += t_duration 
                output.append(tasknum)
                
            candojob = max(candojob, starttime) 
            for tasknum in jobs[starttime]: # 지금시간에 새로 열린 잡들을 풀에 넣는다
                t_start, t_duration = tasks[tasknum]
                heappush(queue, (t_duration, tasknum))
            
        while queue:
            (t_duration, tasknum) = heappop(queue)
            output.append(tasknum)
        return output 
                