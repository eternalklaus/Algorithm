# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            if l1 and l2:
                if l1.val < l2.val:
                    l1.next = merge(l1.next, l2)
                    return l1 
                else:
                    l2.next = merge(l1, l2.next)
                    return l2
            return l1 or l2
        
        return merge(list1, list2)