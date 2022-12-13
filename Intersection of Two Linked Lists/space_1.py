#T: O(N+M) S:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        countA = countB = 0
        while tempA:
            countA+=1
            tempA = tempA.next
        while tempB:
            countB+=1
            tempB = tempB.next
        diff = abs(countA-countB)
        tempA,tempB = (headA,headB) if countA>countB else (headB,headA)
        while diff:
            tempA = tempA.next
            diff-=1
        while tempA and tempA!=tempB:
            tempA= tempA.next
            tempB = tempB.next
        return tempA

#Time :O(N+M)
#Space: O(1)
# Linkedlist
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA,tailA= self.countLen(headA)
        countB,tailB = self.countLen(headB)
        if tailA!= tailB:
            return None
        if countA<countB:
            headA,headB = headB,headA
            countA,countB = countB,countA
        for _ in range(countA-countB):
            headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA,headB = headA.next,headB.next
        return None
    
    def countLen(self,pointer):
        length = 1
        while pointer.next:
            length+=1
            pointer = pointer.next
        return length,pointer
