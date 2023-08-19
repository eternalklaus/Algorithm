# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast, bla bla bla...
        slow, fast = head, head 
        # 마음놓고 null 나올때까지 갈수도 없는 노릇이잖아?
        while fast and fast.next: ###<=
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast: return True 
        return False 