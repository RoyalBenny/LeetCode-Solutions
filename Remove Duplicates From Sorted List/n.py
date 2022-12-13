# Time : O(N)
# Space : O(1)
# Linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not node:
            return head
        prev = node
        node = node.next
        
        while node:
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head
