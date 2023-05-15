#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    nNodes = 0
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def countNodes(node, maxParent):

            if not node:
                return

            if node.val >= maxParent:
                self.nNodes += 1
                maxParent = node.val

            if node.left:
                countNodes(node.left, maxParent)
            if node.right:
                countNodes(node.right, maxParent)
        
        countNodes(root, -float("inf"))
        return self.nNodes


        
# @lc code=end

