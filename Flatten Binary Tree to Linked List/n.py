# Time : O(n)
# Space : O(n)
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        newNode = self.flattenBst(root)[1]
        root.right = newNode.right
        root.left = None
        
    def flattenBst(self,root,node = None, head = None):
        if not root:
            return [node,head]
        if not node:
            node = TreeNode(root.val)
            head = node
        else:
            node.right = TreeNode(root.val)
            node = node.right
        node = self.flattenBst(root.left,node)[0]
        node = self.flattenBst(root.right,node)[0]
        return [node,head]
