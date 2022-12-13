#Time : O(N)
#Space :O(1)
#https://leetcode.com/problems/linked-list-cycle-ii/submissions/
#Linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next or not head.next.next: 
#             return None
#         p1 = head.next
#         p2 = head.next.next
        
#         while p1 and p2 and head != p1 and head != p2:
#             if p1 == p2:
#                 head = head.next
#             p1 = p1.next 
#             if not p2.next:
#                 return None
#             p2 = p2.next.next
#         if p1 and p2:
#             return head
#         return None
        slow,fast = head,head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
