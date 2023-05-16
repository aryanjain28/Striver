#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        mMap = {}
        for index, n in enumerate(inorder):
            mMap[n] = index

        def generateTree(val):

            node = TreeNode(val)     
            # index = inorder.index(val)
            index = mMap[val]
            inorder[index] = None

            if (index > 0 and inorder[index-1] != None):
                node.left = generateTree(preorder.pop(0))

            if (index < len(inorder)-1 and inorder[index+1] != None):
                node.right = generateTree(preorder.pop(0))

            return node
        
        return generateTree(preorder.pop(0))

        
# @lc code=end

