# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop, heapify
        heap = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapify(heap)
        
        fakehead = ListNode()
        prev = fakehead 
        while heap:
            (_, idx) = heappop(heap)
            node = lists[idx]
            
            prev.next = node 
            prev = node 
            
            if node.next:
                lists[idx] = node.next ### 중요!move it
                heappush(heap, (node.next.val, idx)) # idx = borned social hierarchy. it keeps.
        
        return fakehead.next 
        
            