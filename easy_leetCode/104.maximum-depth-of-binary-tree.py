#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root):

        def traverse(node, depth):
            if not node:
                return depth

            return max(traverse(node.left, depth + 1), traverse(node.right, depth + 1))

        return traverse(root, 0)
    

    
# @lc code=end

