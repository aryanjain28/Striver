#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        minimum = 1
        stack = [(root, minimum)]

        while stack:
            node, height = stack.pop(0)

            if not node.left and not node.right:
                return height

            height += 1
            if node.left:
                stack.append((node.left, height))
            if node.right:
                stack.append((node.right, height))


# @lc code=end
