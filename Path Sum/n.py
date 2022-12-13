#T:O(N) S:O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def backtrack(node,total):
            if not node:
                return False
            if not node.left and not node.right:
                return total+node.val==targetSum
            return (backtrack(node.left,total+node.val) or 
                   backtrack(node.right,total+node.val))
        return backtrack(root,0)

#Time : O(N)
#Space : O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int,sum = 0) -> bool:
        if not root:
            return False
        if sum+root.val == targetSum and not root.right and not root.left:
            return True
        return self.hasPathSum(root.left,targetSum,sum+root.val) or
        self.hasPathSum(root.right,targetSum, sum+root.val)
