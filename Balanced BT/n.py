# Time : O(n)
# Space : O(h) 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isBalancedBST = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.checkBalancedBST(root)
        return self.isBalancedBST
    
    def checkBalancedBST(self,root, height = 0):
        if not root:
            return height - 1
        h1 = self.checkBalancedBST(root.left,height+1)
        h2 = self.checkBalancedBST(root.right,height+1)
        
        if(abs(h1-h2) > 1):
            self.isBalancedBST = False
        
        return max(h1,h2)
