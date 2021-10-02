class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq
        heapq.heapify(nums)
        
        return (heapq.nlargest(k, nums))[-1]