# Time: O(n)
# Space : O(1)
# Linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        n = head
        f = head.next
        
        while f and f.next:
            f = f.next.next
            if f:
                n = n.next
        n.next = n.next.next
        return head
