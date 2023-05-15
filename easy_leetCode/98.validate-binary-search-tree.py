#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validateBST(node, min, max):

            if not node:
                return True

            if not min < node.val < max:
                return False
            else:
                return validateBST(node.left, min, node.val) and validateBST(node.right, node.val, max)
        
        return validateBST(root, float("-inf"), float("inf"))


# @lc code=end

