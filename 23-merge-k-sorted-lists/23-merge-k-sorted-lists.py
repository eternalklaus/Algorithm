# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        for i, l in enumerate(lists):
            if not l: continue 
            heapq.heappush(heap, (l.val, i))
        
        fakehead = ListNode()
        node = fakehead 
        while heap:
            (v, i) = heapq.heappop(heap)
            
            node.next = lists[i] # append popped list (minimum value) into node 
            node = node.next 
            
            if lists[i].next:
                lists[i] = lists[i].next # move to next list 
                heapq.heappush(heap, (lists[i].val, i))
        
        return fakehead.next 