#
# @lc app=leetcode id=563 lang=python
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
        
        self.sum = 0
        def calTilt(node):

            if not node:
                return 0
            
            sumL = calTilt(node.left)
            sumR = calTilt(node.right)
            self.sum += abs(sumL - sumR)

            return sumL + sumR + node.val
        
        calTilt(root)
        return self.sum
        
# @lc code=end

