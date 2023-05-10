#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):

        def compare(pnode, qnode):

            if not pnode and not qnode:
                return True
            elif (not pnode or not qnode) or (pnode.val != qnode.val):
                return False

            left = compare(pnode.left, qnode.left)
            right = compare(pnode.right, qnode.right)

            return left and right

        return compare(p, q)


# @lc code=end
