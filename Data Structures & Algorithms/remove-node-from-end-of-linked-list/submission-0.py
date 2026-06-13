# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        fast = head
        countdown = n

        while fast and countdown > 0:
            fast = fast.next
            countdown-=1
        
        slow = head
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev is None:
            return head.next
        prev.next = slow.next

        return head


            