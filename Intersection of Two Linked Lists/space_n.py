#Time :O(N+M)
#Space: O(N)
# Linkedlist
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headASet = set()
        while headA:
            headASet.add(headA)
            headA = headA.next
        
        while headB:
            if headB in headASet:
                return headB
            headB = headB.next
        
        return None
