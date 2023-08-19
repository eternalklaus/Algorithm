# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head 
        head = None 
        
        # Idea: get node from back, and insert it into the very front 
        while node:
            # 1) backup next node 
            nextnode = node.next 
           
            # 2) insert node into the front of linked list 
            node.next = head
            head = node 
            
            # 3) restore next node 
            node = nextnode 
        
        return head