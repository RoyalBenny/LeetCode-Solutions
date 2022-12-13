# Time : O(n)
# Space : O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.createBST(array)
    def createBST(self, array):
        if not array:
            return None
        mid = len(array)//2
        node = TreeNode(array[mid])
        node.left = self.createBST(array[:mid])
        node.right = self.createBST(array[mid+1:])
        return node
