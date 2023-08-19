# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Get middle of list 
        fast, slow = head, head 
        while fast and fast.next:
            prevslow = slow 
            slow = slow.next ### move this first
            fast = fast.next.next 
        # prevslow.next = None 
        middle = slow 
        
        # slow = 1, 2, 3, 4, 5, 6
        # fast = 4, 5, 6
        
        # 2. Reverse second list
        prevnode = None 
        node = middle 
        while node:
            nextnode = node.next 
            node.next = prevnode 
            prevnode = node 
            node = nextnode 
        slow = prevnode # start of node is prevnode 
        # slow = 6, 5, 4
        
        
        # 3. Interleave two lists 
        node1 = head 
        node2 = slow 
        while node2.next:
            node1.next, node1 = node2, node1.next 
            node2.next, node2 = node1, node2.next 