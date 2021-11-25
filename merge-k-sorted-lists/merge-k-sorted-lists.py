# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Gather all nodes - O(N) 
        output = []
        for l in lists:
            while l:
                output.append(l)
                l = l.next 
        
        # Sort all nodes - O(NlogN) 
        output.sort(key=lambda x:x.val)    
        
        # Create linked list - O(N)
        for i, o in enumerate(output):
            if i == len(output) - 1: # last component
                o.next = None 
            else:
                o.next = output[i+1]
        
        return output[0] if output else None