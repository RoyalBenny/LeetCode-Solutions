# Time : O(n)
# Space : O(v)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.nodeSet = set()
        self.LCA = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.findNode(root,p.val)
        self.findAncestor(root,q.val)
        return TreeNode(self.LCA)
    
    def findNode(self,node,val):
        if not node:
            return False
        if node.val == val:
            self.nodeSet.add(node.val)
            return True
        found = self.findNode(node.left,val)
        if not found:
            found = self.findNode(node.right,val)
        if found:
            self.nodeSet.add(node.val)
        return found
    
    def findAncestor(self,node,val):
        if not node:
            return False
        if node.val == val and val in self.nodeSet:
            self.LCA = node.val
            return True
        elif node.val == val:
            return True
        found = self.findAncestor(node.left,val)
        if not found and  self.LCA == None:
            found = self.findAncestor(node.right,val)
        if found and  self.LCA == None and node.val in self.nodeSet:
            self.LCA = node.val
        return found
