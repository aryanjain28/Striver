#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):

        def isMirror(node1, node2):

            if not node1 and not node2:
                return True
            
            elif not node1 or not node2:
                return False

            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node2.left, node1.right)
        
        return isMirror(root.left, root.right)

        
# @lc code=end

