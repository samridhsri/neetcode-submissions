# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We need to use fast and slow pointer method to solve this question

        #This is also called Floyd Warshall Cycle detection algorithm

        fp = head
        sp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next

            if fp == sp:
                return True
        
        return False