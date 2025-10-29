# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        tiebreaker = 0

        for node in lists:
            tiebreaker += 1
            if node: heapq.heappush(heap, (node.val, tiebreaker, node))
        
        head = ListNode()
        curr = head

        while heap:
            tiebreaker += 1
            (val, _, node) = heapq.heappop(heap) # minimum value
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, tiebreaker, node.next))
        
        return head.next

