# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2nodes(node1, node2):
            node1, node2 = node1, node2
            root = ListNode(0)
            node3 = root
            
            while node1 and node2:
                if node1.val <= node2.val:
                    node3.next = node1 
                    node1 = node1.next 
                    node3 = node3.next
                else:
                    node3.next = node2
                    node2 = node2.next
                    node3 = node3.next
                
            node3.next = node1 or node2 
            return root.next 
        
        while len(lists) >= 2:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(merge2nodes(l1, l2))
        
        return lists[0] if lists else None