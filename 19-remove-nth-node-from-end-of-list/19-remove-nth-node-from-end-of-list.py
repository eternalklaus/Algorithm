# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fakehead = ListNode(0, head)
        slow, fast = fakehead, fakehead
        
        # n times of cycle is needed to fill the gap
        cycle = 0
        while fast.next: ###<= 
            if cycle >= n: 
                slow = slow.next 
                fast = fast.next 
            else:
                fast = fast.next 
            cycle += 1
        
        # [[1]]
        slow.next = slow.next.next 
        return fakehead.next
            