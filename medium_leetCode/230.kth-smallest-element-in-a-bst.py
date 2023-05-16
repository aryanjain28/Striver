#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # iteratively
        stack = []
        res = []

        while len(res) < k:

            if not root:
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                stack.append(root)
                root = root.left

        return res[k-1]

        # recursively
        # def traverse(node):

        #     if not node:
        #         return []
            
        #     return traverse(node.right) + [node.val] + traverse(node.left)

        # return traverse(root)[-k]
        
# @lc code=end

