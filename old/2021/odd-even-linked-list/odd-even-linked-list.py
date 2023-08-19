# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ohead = ListNode()
        ehead = ListNode()
        oenode = [ohead, ehead] # 0, 1
        node = head 
        
        i = 0
        while node:
            oenode[i].next = node 
            oenode[i] = oenode[i].next 
            
            node = node.next 
            i ^= 1 
            
        oenode[0].next = ehead.next 
        oenode[1].next = None 
        return ohead.next 