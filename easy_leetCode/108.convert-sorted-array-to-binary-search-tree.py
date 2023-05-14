#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def arrToBinTree(arr):

            LEN = len(arr)
            if LEN <= 1:
                return TreeNode(arr[0]) if LEN == 1 else None

            mid = LEN // 2
            return TreeNode(arr[mid], arrToBinTree(arr[:mid]), arrToBinTree(arr[mid+1:]))
            
        return arrToBinTree(nums)


        



        

        
# @lc code=end

