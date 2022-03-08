# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1 or not l2: return l1 or l2
            # l1 should always be smaller one 
            if l1.val > l2.val: l1, l2 = l2, l1 
            head = l1 
            
            while l1.next and l1.next.val < l2.val:
                l1 = l1.next 
            
            l1next, l2next = l1.next, l2.next 
            l1.next = l2 
            l2.next = merge(l1next, l2next)
            return head

        
        if not lists: return None
        head = lists.pop()
        while lists:
            tail = lists.pop()
            head = merge(head, tail)
        return head