# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If list1 or list2 are empty
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        # Create an empty linked list for the result

        result = ListNode()

        #Iterate to both of the lists while comparing each element with each other and adding them to result

        #p1 goes from list1 and p2 goes from list2

        p1 = list1
        p2 = list2
        curr = result

        while p1 and p2:
            if(p1.val < p2.val):
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        while p1:
            curr.next = p1
            p1 = p1.next
            curr = curr.next
        
        while p2:
            curr.next = p2
            p2 = p2.next
            curr = curr.next
        
        return result.next
        