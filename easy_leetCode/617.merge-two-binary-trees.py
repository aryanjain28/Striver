#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, node1, node2) :

        if not node1:
            return node2 
        elif not node2:
            return node1
        
        node1.val += node2.val
        node1.left = self.mergeTrees(node1.left, node2.left)
        node1.right = self.mergeTrees(node1.right, node2.right)
        
        return node1        
        
# @lc code=end

