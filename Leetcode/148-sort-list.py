# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # top-down merge sort 
        if head is None or head.next is None:
            return head 
        
        # split
        node1 = head 
        node2 = self.getMid(head)
        # sort
        head1 = self.sortList(node1)
        head2 = self.sortList(node2)
        # merge
        return self.merge(head1, head2)
    
    def merge(self, head1, head2): 
        head3 = ListNode()
        node = head3
        while head1 and head2:
            if head1.val <= head2.val:
                node.next, node, head1 = head1, head1, head1.next
            else: 
                node.next, node, head2 = head2, head2, head2.next
        
        node.next = head1 or head2 # wow
        return head3.next

    def getMid(self, head):
        fast, slow = head, head 
        while fast.next and fast.next.next:
            fast = fast.next.next 
            slow = slow.next 
        
        midd = slow.next # wow 
        slow.next = None 
        
        return midd

            
