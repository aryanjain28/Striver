#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root, subRoot):

        def isSub(node, subNode):

            if not subNode and not node:
                return True
            
            if not subNode or not node:
                return False

            if subNode.val != node.val:
                return False
            
            nodeL = isSub(subNode.left, node.left)
            nodeR = isSub(subNode.right, node.right)
            
            return nodeL and nodeR
        
        if not root:
            return False 
        elif isSub(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
# @lc code=end

