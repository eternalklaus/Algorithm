# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ### [[]] is different from []
        
        # 1. Remove empty list from lists
        L = len(lists)
        for i in range(L-1, -1, -1):
            if not lists[i]:
                lists.pop(i)
        
        # 2. Interleave all element of list into one large linked list 
        fakehead = ListNode(0)
        prevnode = fakehead 
        
        while lists:
            lists.sort(key=lambda x:x.val)
            # pop least value node and append it into output 
            node = lists.pop(0)
            prevnode.next = node
            # move prevnode
            prevnode = node 
            
            if node.next: # Repush node into lists only if node has next.
                lists.append(node.next)
        
        return fakehead.next 