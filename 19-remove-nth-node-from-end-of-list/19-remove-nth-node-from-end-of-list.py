# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # keep queue in size n+1, if more then n, remove the front component. 
        # in the end, cut node[1] using node[0]
        def printqueue(queue):
            for q in queue:
                print ('%d '% q.val, end='')
            print ('')
        
        fakehead = ListNode(-1, head)
        node = fakehead  
        queue = []
        
        while node: 
            queue.append(node)
            if len(queue) > n + 1: # queue contains [node - 1] [node] 
                queue.pop(0)
            # printqueue(queue)
            node = node.next
        
        queue[0].next = queue[1].next 
        return fakehead.next 
            