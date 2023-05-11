#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):

        def check(node):

            if not node:
                return 0

            heightL = check(node.left)
            heightR = check(node.right)

            if heightL == -1 or heightR == -1 or abs(heightL - heightR) > 1:
                return -1
            
            return max(heightL, heightR) + 1

        return check(root) >= 0

        # if (not root):
        #     return True        
        
        # def depth(node):

        #     if not node: 
        #         return 0
            
        #     return max(depth(node.left) + 1, depth(node.right) + 1)

        # def check(nodeL, nodeR):

        #     depthL = depth(nodeL)
        #     depthR = depth(nodeR)
        #     depthDiff = abs(depthL - depthR)

        #     if depthL == 0 or depthR == 0:
        #         return depthDiff <= 1

        #     if depthDiff > 1:
        #         return False
            
        #     checkL = check(nodeL.left, nodeL.right)
        #     checkR = check(nodeR.left, nodeR.right)

        #     return checkL and checkR


        # return check(root.left, root.right)
         
        
# @lc code=end

