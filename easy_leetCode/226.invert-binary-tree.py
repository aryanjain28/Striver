#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        
        def invert(node):

            if not node:
                return None
            
            # leaf
            if not node.left and not node.right:
                return node
            
            tempL = invert(node.left)
            tempR = invert(node.right)
            
            node.left, node.right = tempR, tempL
            return node


        if not root:
            return None

        tempL = invert(root.left)
        tempR = invert(root.right)
            
        root.left, root.right = tempR, tempL
        return root
        
# @lc code=end

