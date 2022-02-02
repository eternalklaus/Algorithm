# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fakehead = ListNode()
        node = fakehead 
        
        heap = [(x.val, idx) for idx, x in enumerate(lists) if x]
        heapify(heap)
        
        
        while heap:
            (val, idx) = heappop(heap)
            leastnode = lists[idx]
            
            node.next = leastnode
            node = leastnode 
            
            if leastnode.next:
                lists[idx] = leastnode.next
                heappush(heap, (leastnode.next.val, idx))
        
        return fakehead.next 