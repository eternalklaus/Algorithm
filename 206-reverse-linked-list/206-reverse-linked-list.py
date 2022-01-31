# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # deal empty list 
        if not head: return head 
        
        node = head.next 
        head.next = None # end of node
        
        # get node from back, and insert it into the very front 
        while node:
            nextnode = node.next 
           
            # insert node into the front of linked list 
            node.next = head
            head = node 
            
            node = nextnode 
        
        return head