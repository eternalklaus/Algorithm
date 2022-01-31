# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-101) 
        node = head 
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next 
            else:
                node.next = l2
                l2 = l2.next 
            # move to next node 
            node = node.next 
            
        # append remaining nodes 
        leftnodes = l1 or l2 
        node.next = leftnodes
                
        return head.next 