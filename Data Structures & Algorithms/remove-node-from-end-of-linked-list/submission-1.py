# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        countdown = n

        

        while countdown > 0:
            fast = fast.next
            countdown-=1
        
        if not fast:
            return head.next
        slow = head
        prev = None

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        # Remove the slow pointer from the list
        prev.next = slow.next
        slow.next = None

        return head