#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def diameterOfBinaryTree(self, root):
        
        self.res = 0
        def depth(node):

            if not node:
                return 0

            depthL = depth(node.left)
            depthR = depth(node.right)
            self.res = max(self.res, depthL + depthR)
            return max(depthL, depthR) + 1
            
        depth(root)
        return self.res
        
# @lc code=end

