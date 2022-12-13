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
        lHead,lTail = None, None
        hHead,hTail = None,None
        
        while head:
            if head.val < x:
                if not lHead:
                    lHead = head
                    lTail = lHead
                    
                else:
                    lTail.next = head
                    lTail = lTail.next
                    
            else:
                
                if not hHead:
                    hHead = head
                    hTail = hHead
                    
                else:
                    hTail.next = head
                    hTail = hTail.next
                    
            head = head.next

        if lHead and hHead:
                lTail.next = hHead
                hTail.next = None
                return lHead
        if lHead:
                return lHead
        return hHead
                
            
                    
                    
