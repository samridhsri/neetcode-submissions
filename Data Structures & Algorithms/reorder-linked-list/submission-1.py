# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fp, sp = head, head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        
        curr, prev = sp, None

        while curr.next:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        curr.next = prev

        first, second = head, curr

        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2
        