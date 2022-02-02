# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sort 쓰는 방법
        # heapq 쓰는 방법 -> min heap -> logn
        
        fakehead = ListNode()
        node = fakehead 
        # trim useless nodes 
        heap = [(x.val, idx) for idx, x in enumerate(lists) if x]
        heapify(heap) # => min heap based on x.val 
        
        while heap:
            (val, idx) = heappop(heap)
            minlist = lists[idx]
            node.next = minlist 
            node = minlist 
            
            if minlist.next:
                heappush(heap, (minlist.next.val, idx))
                lists[idx] = minlist.next 
        
        node.next = None 
        
        return fakehead.next 