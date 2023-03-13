#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != 0:
                i += 1
            elif nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

# @lc code=end
