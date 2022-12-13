#Time : O(N)
#Space: O(V)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.LCA = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root,p,q)
        return  TreeNode(self.LCA)
    
    def dfs(self,node,p,q):
        if not node:
            return False
        if self.LCA:
            return False
        check = p == node or q == node
        found1 = self.dfs(node.left,p,q)
        found2 = self.dfs(node.right,p,q)
        
        if (found1 and found2) or (found1 and check) or (found2 and check):
            self.LCA = node.val
        return check or found1 or found2
    
    
