class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, output = [], []
        
        # clean useless one <-
        def clean_weak(deq, n):
            while deq:
                i = deq.pop()
                if nums[i] < n: # it deserve to be poped
                    continue 
                else: 
                    deq.append(i)
                    break
            return 
        
        # clean useless one ->
        def clean_dead(deq, newi):
            while deq:
                oldi = deq.pop(0)
                if newi - oldi >= k: # generation gap.. 
                    continue 
                else: 
                    deq.insert(0, oldi)
                    break
            return 
        
        for i, n in enumerate(nums):
            # eliminate older, weaker one
            clean_weak(deq, n)
            
            # take seat in the queue
            deq.append(i)
            
            if i >= k-1:
                # pick leftmost element from deq
                clean_dead(deq, i)
                output.append(nums[deq[0]])
            
        return output
            