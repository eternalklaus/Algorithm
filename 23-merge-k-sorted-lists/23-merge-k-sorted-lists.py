# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time complexity: O(n) assuming n is length of list l1
        def merge(l1, l2):
            if not l1 or not l2: return l1 or l2
            if l1.val > l2.val: l1, l2 = l2, l1 # pick smaller one as l1
            head = l1 
            
            while l1.next and l1.next.val < l2.val:
                l1 = l1.next 
            
            l1next, l2next = l1.next, l2.next 
            l1.next = l2 
            l2.next = merge(l1next, l2next)
            return head
        
        # time complexity: log(k) given k is total number of linked list
        if not lists: return None
        
        while len(lists) >= 2: ### merge 할 때, 2개씩 뽑아야 TC O(logk)임. 1개씩 뽑는다면 O(k)
            head = lists.pop()
            tail = lists.pop()
            lists.append(merge(head, tail))
        return lists[0]