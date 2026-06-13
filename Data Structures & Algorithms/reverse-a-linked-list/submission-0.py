# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: #When the list is empty
            return None
        
        prev = None
        curr = head

        while(curr.next!=None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        curr.next = prev # For the last Node
        head = curr
        return head  