#Time : O(n)
# Space: O(1)
# Linkedlist
#https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-Linked-list/1#

def getNthFromLast(head,n):
    #code here
    node = head
    length = 0
    while node:
        length += 1
        node = node.next
    if length < n :
        return -1
    pos = length - n 
    length = 0
    node = head
    while length < pos:
        node = node.next
        length+=1
    return node.data

def getNthFromLast(head,n):
    #code here
    temp = head
    while head:
        if n >0:
            n-=1
        else:
            temp = temp.next
        head = head.next
    if n > 0:
        return -1
    return temp.data
