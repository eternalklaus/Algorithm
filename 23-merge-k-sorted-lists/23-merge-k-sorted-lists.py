# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fakehead = ListNode()
        node = fakehead 
        
        lists = [x for x in lists if x]
        
        while lists:
            lists.sort(key=lambda x:x.val)
            leastnode = lists.pop(0)
            
            node.next = leastnode
            node = leastnode 
            
            if leastnode.next:
                lists.append(leastnode.next) 
        
        return fakehead.next 