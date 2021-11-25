# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # gather all nodes
        output = []
        for l in lists:
            while l:
                output.append(l)
                l = l.next 
        
        output.sort(key=lambda x:x.val)
        for i, o in enumerate(output):
            if i == len(output) - 1: # last component
                o.next = None 
            else:
                o.next = output[i+1]
        
        if output:
            return output[0]
        else:
            return None
            