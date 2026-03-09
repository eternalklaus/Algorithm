class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque를 쓰면 쉽게 풀린다고? 
        heap = [] # max heap
        counter = Counter() # 윈도우에 들어가 있는 값들의 카운트를 저장하는 저장소
        left = 0
        right = -1
        output = []
        
        # O(Nlog(k))
        while True:
            right += 1
            if right >= len(nums): break 

            counter[nums[right]] += 1
            heappush(heap, -nums[right]) # O(logk)
            
            if right - left + 1 < k: # 윈도우가 점점 커져가는 phase
                continue 
            
            if right - left + 1 == k:
                while counter[-heap[0]] == 0:
                    heappop(heap) # O(logk)
                output.append(-heap[0]) 

                counter[nums[left]] -= 1
                left += 1
            
        return output