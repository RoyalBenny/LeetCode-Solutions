# Time : O(n)
# Spacce : O(h) h->height of tree
#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/

# T: O(N) S:O(H)
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
        def dfs(root):
            if not root:
                return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            return rightTail or leftTail or root
        
        dfs(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.end = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            self.end = root
            return
        self.flatten(root.left)
        if self.end and root.left:
            right = root.right
            root.right = root.left
            self.end.right = right
            root.left = None
            self.flatten(self.end.right)
        else:
            self.flatten(root.right)
        
