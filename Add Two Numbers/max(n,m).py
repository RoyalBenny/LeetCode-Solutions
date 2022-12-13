R#Time :O(max(n,m))
#Space : O(max(n,m))
# Linkedlist
# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(-1)
        carry,end = 0,output
        
        while l1 and l2:
            end,carry = self.addNode(end,carry+l1.val+l2.val)
            l1,l2 = l1.next,l2.next
        
        while l1:
            end,carry = self.addNode(end,carry+l1.val)
            l1 = l1.next
        
        while l2:
            end,carry = self.addNode(end,carry+l2.val)
            l2 = l2.next
        
        if carry > 0:
            self.addNode(end,carry)
        
        return output.next
    
    def addNode(self,end,val):
        carry,val = val//10, val%10
        end.next = ListNode(val)
        return end.next,carry
