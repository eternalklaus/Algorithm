# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random 

    def __init__(self, head: Optional[ListNode]):
        self.head = head 

    def getRandom(self) -> int:
        node = self.head 
        i, output = 1, node.val
        while node:
            pickthis = random.randrange(0, i) == 0 # 0/1 1/2 2/3

            if pickthis:
                output = node.val

            i = i+1
            node = node.next
        return output
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()