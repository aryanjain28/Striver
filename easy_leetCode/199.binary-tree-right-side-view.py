#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        res = []
        queue = [[root]]
        while queue:
            temp = []
            
            nodes = queue.pop(0)
            res.append(nodes[-1].val)

            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if temp:
                queue.append(temp)

        return res




        
# @lc code=end

