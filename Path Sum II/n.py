#Time : O(N)
#Space: O(pathlen)
# binary tree
# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return self.output
        self.pathCal(root,targetSum)
        return self.output
         
    def pathCal(self, root: Optional[TreeNode], targetSum: int, nodes = [],sum = 0) -> List[List[int]]:
        if not root:
            return 
        nodes.append(root.val)
        total = sum+root.val
        if total == targetSum and not root.right and not root.left:
            self.output.append(nodes.copy())
        else:
            self.pathCal(root.left,targetSum,nodes, total)
            self.pathCal(root.right, targetSum,nodes,total)
        nodes.pop(-1)
