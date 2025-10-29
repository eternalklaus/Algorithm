# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while True:
            if fast == None or fast.next == None or fast.next.next == None: return False
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow: return True