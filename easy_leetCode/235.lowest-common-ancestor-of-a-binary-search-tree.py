#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)
       
        if minimum <= root.val <= maximum:
            return root
        
        elif root.val <= minimum:
            return self.lowestCommonAncestor(root.right, p, q)

        elif root.val >= maximum:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root, p, q)
    
                    
        # while True:

        #     if minimum <= root.val <= maximum:
        #         return root
        #     elif root.val <= minimum:
        #         root = root.right
        #     elif root.val >= maximum:
        #         root = root.left



            
        
# @lc code=end

