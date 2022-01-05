class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counter = Counter(tasks)
        total, result = len(tasks), 0
        while total:
            keys = sorted(counter.keys(), key=lambda x:-counter[x])
            cycletasks = 0
            for task in keys:
                if cycletasks == n + 1:break
                # print (task)
                counter[task] -= 1
                cycletasks += 1
                total -= 1
                if counter[task] == 0: del counter[task]
            
            # print ("%d slot passed" % (n+1))
            if total: 
                result += (n + 1) 
            else: # we finished the last cycle
                result += cycletasks 
        
        return result
