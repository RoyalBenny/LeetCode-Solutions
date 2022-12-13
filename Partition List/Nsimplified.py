#Time : O(N)
#Space : O(1)
# LinkedList
# https://leetcode.com/problems/partition-list/
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def partition(head, x):
        if not head:
            return None
        lHead,hHead = ListNode(-1),ListNode(-1)
        lTail,hTail = lHead,hHead
        
        while head:
            if head.val < x:
                    lTail.next = head
                    lTail = lTail.next
                    
            else:
                    hTail.next = head
                    hTail = hTail.next
                    
            head = head.next

        lTail.next = hHead.next
        hTail.next = None
        return lHead.next
            
                    
                    
