# Time : O(n)
# Space : O(d)
# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self,tree,max = float("Inf"), min = float("-Inf")):
        # Write your code here.
        if not tree:
            return True
        if tree.val <= min or tree.val >= max:
            return False
        return self.isValidBST(tree.left,tree.val,min) and self.isValidBST(tree.right,max, tree.val)
        
