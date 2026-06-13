# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        if head is None:
            return None

        while (curr.next != None):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        curr.next = prev
        head = curr
        return head