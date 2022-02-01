# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sort 쓰는 방법
        # heapq 쓰는 방법 
        
        fakehead = ListNode()
        node = fakehead 
        # trim useless nodes 
        lists = [l for l in lists if l] # remove empty node 
        while lists:
            lists.sort(key=lambda l:l.val) # sort by value 
            minlist = lists.pop(0)
            node.next = minlist 
            node = minlist 
            
            if minlist.next:
                lists.append(minlist.next)
        node.next = None 
        
        return fakehead.next 