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
        def connect(node1, node2):
            # print ('%d -> %d' % (node1.val, node2.val))
            node1.next = node2 
            node2.next = None 

        # Single loop? no.
        linkedlist = []
        node = head 
        while node:
            linkedlist.append(node)
            node = node.next 
        
        
        total = len(linkedlist)
        # print (linkedlist, total)
        i = 0
        First = ListNode()
        prev = First 

        while True:
            connect(prev, linkedlist[i])
            if i >= total-1-i: break 
            connect(linkedlist[i], linkedlist[total-1-i])
            
            prev = linkedlist[total-1-i]
            i += 1